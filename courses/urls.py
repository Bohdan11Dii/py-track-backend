from django.urls import path
from courses.views import index, ModuleListView, ModuleCreateView, ModuleDeleteView, ModuleUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('modules/', ModuleListView.as_view(), name='module-list'),
    path('modules/create/', ModuleCreateView.as_view(), name='module-create'),
    path('modules/<slug:slug>/update', ModuleUpdateView.as_view(), name='module-update'),
    path('modules/<slug:slug>/delete', ModuleDeleteView.as_view(), name='module-delete'),

]

app_name = 'courses'
