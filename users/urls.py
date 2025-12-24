from django.urls import path
from users.views import CreateUserView, CustomLoginView, profile, custom_logout

urlpatterns = [
    path('registration/', CreateUserView.as_view(), name='registration'),
    path("profile/", profile, name="profile"),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),

]

app_name = 'users'
