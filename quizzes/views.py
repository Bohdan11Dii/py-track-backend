from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from quizzes.models import Test
from quizzes.forms import TestForm


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


class TestUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Test
    form_class = TestForm
    template_name = "quizzes/test/test_form.html"
    success_url = reverse_lazy("quizzes:test-list")


class TestDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Test
    template_name = "quizzes/test/test_confirm_delete.html"
    success_url = reverse_lazy("quizzes:test-list")
