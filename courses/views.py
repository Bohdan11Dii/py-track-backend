from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from courses.forms import ModuleForm
from courses.models import Module


def index(request):
    return render(request, "courses/module/index.html")


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
