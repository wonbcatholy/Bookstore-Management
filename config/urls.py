from django.contrib import admin
from django.urls import path
from apps.common import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("health/", views.health_check, name="health_check"),
]
