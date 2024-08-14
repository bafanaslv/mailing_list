from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import (UserCreateView, email_verification, password_reset_request,
                         ProfileView, UsersListView, UserUpdateView, UserDetailView, UserProfileUpdateView,
                         UserDeleteView)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>', email_verification, name='email-confirm'),
    path('password-reset/', password_reset_request, name='password_reset'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('<int:pk>/user_update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/user_profile/', UserDetailView.as_view(), name='user_profile'),
    path('<int:pk>/user_profile_update/', UserProfileUpdateView.as_view(), name='user_update_profile'),
    path('<int:pk>/use_delete/', UserDeleteView.as_view(), name='user_delete'),
]
