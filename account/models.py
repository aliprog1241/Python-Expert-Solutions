from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    zoom_url = models.CharField(
        max_length=500,
        default="https://zoom.us"   # پیش‌فرض برای رکوردهای قدیمی
    )
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="leading_teams",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="members"
    )

    def __str__(self):
        return self.user.username


class Meeting(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="meetings"
    )
    title = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    zoom_url = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} ({self.team.name})"
