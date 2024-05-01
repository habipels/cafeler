from django.shortcuts import render,redirect
from .forms import *
from kategoriler.models import *
def site_bilgileri():
    sozluk = {}
    return sozluk
# Create your views here.
def admin_homebase(request):
    content = site_bilgileri()
    return render(
        request=request,
        template_name="admin_temp/admin_index.html",
        context=content
        )

def logo_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = logo_ekle(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["logolar"] = sayfa_logosu.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:logo_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_logo.html",
        context=content
        )

def logo_sileme(request,id):
    sayfa_logosu.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:logo_duzenleme_sayfasi")



def icon_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = icon(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = sayfa_iconu.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:icon_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_icon.html",
        context=content
        )

def icon_sileme(request,id):
    sayfa_iconu.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:icon_duzenleme_sayfasi")