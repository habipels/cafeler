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
    #eposta adres
    path("settings/epostaadresi", views.eposta_duzenleme_sayfasi, name="eposta_duzenleme_sayfasi"),
    path("settings/epostaadresi/<int:id>", views.eposta_sileme, name="eposta_sileme"),
    #insta
    path("settings/instadresi", views.instagram_duzenleme_sayfasi, name="instagram_duzenleme_sayfasi"),
    path("settings/instaadresi/<int:id>", views.insta_sileme, name="insta_sileme"),
    #banner
    path("settings/banner", views.banner_duzenleme_sayfasi, name="banner_duzenleme_sayfasi"),
    path("settings/banner/<int:id>", views.banner_sileme, name="banner_sileme"),
    #hakkımızda
    path("settings/hakkimizdaduzeltme", views.hakkimizda_duzenleme_sayfasi, name="hakkimizda_duzenleme_sayfasi"),
    #bölgeler
    path("settings/bolgeler", views.bolgeler_duzenleme_sayfasi, name="bolgeler_duzenleme_sayfasi"),
    path("settings/bolgeler/<int:id>", views.bolgeler_sileme, name="bolgeler_sileme"),
    #Menü
    path("settings/menu", views.menu_duzenleme_sayfasi, name="menu_duzenleme_sayfasi"),
    path("settings/menu/<int:id>", views.menu_sileme, name="menu_sileme"),
    #Masa
    path("settings/masa", views.masa_duzenleme_sayfasi, name="masa_duzenleme_sayfasi"),
    path("settings/masa/<int:id>", views.masa_sileme, name="masa_sileme"),
]