from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

urlpatterns = [
    path('', index, name='index'),   # 👈 صفحه اول سایت
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('home/', include('account.urls')),   # می‌تونی اینو بعداً اصلاح کنی
]
