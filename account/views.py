from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods
from .forms import RegisterForm, LoginForm, TeamForm
from .models import Team, UserProfile


# ویو home
@require_GET
@login_required
def home(request):
    user_profile = request.user.userprofile
    team_name = user_profile.team.name if user_profile.team else "None"
    return render(request, 'home.html', {'team_name': team_name})


# ویو register
@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('join_or_create_team')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# ویو login
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


