from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from courses.forms import ModuleForm, TopicForm
from courses.models import Module, Topic


def index(request):
    return render(request, "courses/module/index.html")


# Make CRUD for Module models
class ModuleListView(generic.ListView):
    model = Module
    template_name = "courses/module/module_list.html"


class ModuleCreateView(generic.CreateView):
    model = Module
    form_class = ModuleForm
    template_name = "courses/module/module_form.html"
    success_url = reverse_lazy("courses:module-list")


class ModuleUpdateView(generic.UpdateView):
    model = Module
    form_class = ModuleForm
    template_name = "courses/module/module_form.html"
    success_url = reverse_lazy("courses:module-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ModuleDeleteView(generic.DeleteView):
    model = Module
    template_name = "courses/module/module_confirm_delete.html"
    success_url = reverse_lazy("courses:module-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


# Make CRUD for Topic models
class TopicListView(generic.ListView):
    model = Topic
    queryset = Topic.objects.select_related('module').order_by('order')
    template_name = "courses/topic/topic_list.html"


class TopicCreateView(generic.CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "courses/topic/topic_form.html"
    success_url = reverse_lazy("courses:topic-list")

    def get_queryset(self):
        return Topic.objects.select_related('module')


class TopicUpdateView(generic.UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "courses/topic/topic_form.html"
    success_url = reverse_lazy("courses:topic-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class TopicDeleteView(generic.DeleteView):
    model = Topic
    template_name = "courses/topic/topic_confirm_delete.html"
    success_url = reverse_lazy("courses:topic-list")
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
