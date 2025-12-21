from django import forms

from courses.models import Module, Topic


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'order', 'module']
