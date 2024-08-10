import random
import string
from msilib.schema import ListView
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from mailing.utils import ContextMixin
from users.forms import UserRegisterForm, PasswordResetForm, UserProfileForm
from users.models import User
import secrets
from config.settings import EMAIL_HOST_USER
from django.contrib import messages


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейти по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[EMAIL_HOST_USER]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserLoginView(LoginView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")


def logout_view(request):
    logout(request)
    return redirect("/")


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = generate_password()
                user.password = make_password(new_password)
                user.save()
                try:
                    send_mail(
                        'Восстановление пароля',
                        f'Ваш новый пароль: {new_password}',
                        EMAIL_HOST_USER,
                        [EMAIL_HOST_USER],
                        fail_silently=False,
                    )
                    messages.success(request, f'Новый пароль отправлен на почтовый ящик {EMAIL_HOST_USER}')
                except Exception as e:
                    messages.error(request, 'Ошибка при отправке письма. Попробуйте еще раз.')
                return redirect('users:login')
            except User.DoesNotExist:
                messages.error(request, f'Пользователь с почтой {EMAIL_HOST_USER} не существует')
    else:
        form = PasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')


class UsersListView(ContextMixin, ListView):
    model = User
    template_name = "users_list.html"

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_main_data(**kwargs)
        return context
