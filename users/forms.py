from django.forms import forms, EmailField, ModelForm
from mailing.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'company', 'phone')


class PasswordResetForm(forms.Form):
    email = EmailField(label="Email", max_length=254)


class UserProfileForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('company', 'phone', 'email', 'first_name', 'last_name', 'phone', 'avatar')


class UserUpdateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
