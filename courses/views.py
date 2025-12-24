from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from courses.forms import ModuleForm, TopicForm
from courses.models import Module, Topic
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    return render(request, "courses/module/index.html")


# Make CRUD for Module models
class ModuleListView(LoginRequiredMixin, generic.ListView):
    model = Module
    template_name = "courses/module/module_list.html"


class ModuleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Module
    form_class = ModuleForm
    template_name = "courses/module/module_form.html"
    success_url = reverse_lazy("courses:module-list")


class ModuleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Module
    form_class = ModuleForm
    template_name = "courses/module/module_form.html"
    success_url = reverse_lazy("courses:module-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ModuleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Module
    template_name = "courses/module/module_confirm_delete.html"
    success_url = reverse_lazy("courses:module-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


# Make CRUD for Topic models
class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    queryset = Topic.objects.select_related('module').order_by('order')
    template_name = "courses/topic/topic_list.html"


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "courses/topic/topic_form.html"
    success_url = reverse_lazy("courses:topic-list")

    def get_queryset(self):
        return Topic.objects.select_related('module')


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "courses/topic/topic_form.html"
    success_url = reverse_lazy("courses:topic-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "courses/topic/topic_confirm_delete.html"
    success_url = reverse_lazy("courses:topic-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
