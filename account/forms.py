from django import forms
from django.contrib.auth.models import User
from .models import Team


# فرم ثبت‌نام کاربر جدید
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# فرم ورود
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


# فرم تیم (ایجاد یا پیوستن به تیم)
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'zoom_url']
