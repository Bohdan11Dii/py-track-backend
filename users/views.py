from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from users.forms import UserRegistration
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

"""Реєстрація нового користувача"""


class CreateUserView(generic.CreateView):
    form_class = UserRegistration
    template_name = "registration/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


@login_required
def profile(request):
    return render(request, "users_profile/profile.html")


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # твій шаблон

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return reverse_lazy('courses:index')
        return reverse_lazy('users:profile')


def custom_logout(request):
    logout(request)
    return redirect("users:login")  # або куди хочеш після logout
