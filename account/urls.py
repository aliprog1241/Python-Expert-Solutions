from django.urls import path
from .views import home, register, login, logout, join_or_create_team, leave_team, manage_team

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('team/', join_or_create_team, name='join_or_create_team'),
    path('leave/', leave_team, name='leave_team'),
    path('team/manage/<int:team_id>/', manage_team, name='manage_team'),
]
