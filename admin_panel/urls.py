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
    #site isimleri
    path("settings/isletmeadi", views.isim_duzenleme_sayfasi, name="isim_duzenleme_sayfasi"),
    path("settings/isletmeadi/<int:id>", views.isim_sileme, name="isim_sileme"),
    #Numaraları
    path("settings/isletmenumarasi", views.numara_duzenleme_sayfasi, name="numara_duzenleme_sayfasi"),
    path("settings/isletmenumarasi/<int:id>", views.numara_sileme, name="numara_sileme"),
    #adres
    path("settings/adresi", views.adres_duzenleme_sayfasi, name="adres_duzenleme_sayfasi"),
    path("settings/adresi/<int:id>", views.adres_sileme, name="adres_sileme"),
     #adres
    path("settings/epostaadresi", views.eposta_duzenleme_sayfasi, name="eposta_duzenleme_sayfasi"),
    path("settings/epostaadresi/<int:id>", views.eposta_sileme, name="eposta_sileme"),
]