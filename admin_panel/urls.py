from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = "admin_panel"
urlpatterns = [
    path("dashboard", views.admin_homebase, name="dashboard"),
    #ayarlar
    path("settings/logo", views.logo_duzenleme_sayfasi, name="logo_duzenleme_sayfasi"),
    path("settings/logo/<int:id>", views.logo_sileme, name="logo_sileme"),
    #icon
    path("settings/icon", views.icon_duzenleme_sayfasi, name="icon_duzenleme_sayfasi"),
    path("settings/icon/<int:id>", views.icon_sileme, name="icon_sileme"),
]