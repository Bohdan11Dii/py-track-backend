from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from quizzes.models import Test
from quizzes.forms import TestForm

from quizzes.tasks import parse_test_file


# Create your views here.


class TestListView(LoginRequiredMixin, generic.ListView):
    model = Test
    template_name = "quizzes/test/test_list.html"

    def get_queryset(self):
        return Test.objects.select_related('topic')


class TestCreateView(LoginRequiredMixin, generic.CreateView):
    model = Test
    form_class = TestForm
    template_name = "quizzes/test/test_form.html"
    success_url = reverse_lazy("quizzes:test-list")

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.object.source_file:
            parse_test_file.delay(self.object.pk)

        return response


class TestUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Test
    form_class = TestForm
    template_name = "quizzes/test/test_form.html"
    success_url = reverse_lazy("quizzes:test-list")

    def form_valid(self, form):
        # 1️⃣ Якщо файл змінився — видаляємо старі питання
        if self.object.pk and 'source_file' in form.changed_data:
            self.object.questions.all().delete()

        response = super().form_valid(form)

        # 2️⃣ Запускаємо імпорт нового файлу
        if 'source_file' in form.changed_data and self.object.source_file:
            parse_test_file.delay(self.object.pk)

        return response


class TestDetailView(LoginRequiredMixin, generic.DetailView):
    model = Test
    context_object_name = "test"
    template_name = "quizzes/test/test_detail.html"

    def get_queryset(self):
        return (
            Test.objects
            .select_related('topic')  # FK → OK
            .prefetch_related(
                'questions',
                'questions__answers'
            )
        )


class TestDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Test
    template_name = "quizzes/test/test_confirm_delete.html"
    success_url = reverse_lazy("quizzes:test-list")
