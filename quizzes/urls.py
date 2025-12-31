from django.urls import path, include
from quizzes.views import TestListView, TestCreateView, TestUpdateView, TestDeleteView

urlpatterns = [
    path("tests/", TestListView.as_view(), name='test-list'),
    path("tests/create/", TestCreateView.as_view(), name='test-create'),
    path("tests/update/<int:pk>/", TestUpdateView.as_view(), name='test-update'),
    path("tests/delete/<int:pk>/", TestDeleteView.as_view(), name='test-delete'),

]

app_name = 'quizzes'
