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


