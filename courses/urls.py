from django.urls import path
from courses.views import index, ModuleListView, ModuleCreateView, ModuleDeleteView, ModuleUpdateView, TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('modules/', ModuleListView.as_view(), name='module-list'),
    path('modules/create/', ModuleCreateView.as_view(), name='module-create'),
    path('modules/<slug:slug>/update', ModuleUpdateView.as_view(), name='module-update'),
    path('modules/<slug:slug>/delete', ModuleDeleteView.as_view(), name='module-delete'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('topics/create/', TopicCreateView.as_view(), name='topic-create'),
    path('topics/<slug:slug>/update', TopicUpdateView.as_view(), name='topic-update'),
    path('topics/<slug:slug>/delete', TopicDeleteView.as_view(), name='topic-delete'),

]

app_name = 'courses'
