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


def isim_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = site_isimleri(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = site_adi.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:isim_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_isim.html",
        context=content
        )

def isim_sileme(request,id):
    site_adi.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:isim_duzenleme_sayfasi")


def numara_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = isletmenumarasi(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = numara.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:numara_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_numara.html",
        context=content
        )

def numara_sileme(request,id):
    numara.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:numara_duzenleme_sayfasi")



def adres_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = adresi(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = adres.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:adres_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_adres.html",
        context=content
        )

def adres_sileme(request,id):
    adres.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:adres_duzenleme_sayfasi")



def eposta_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = eposta(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = email_adres.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:eposta_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_eposta.html",
        context=content
        )

def eposta_sileme(request,id):
    email_adres.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:eposta_duzenleme_sayfasi")

def instagram_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = insta(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = sosyalmedyaInsgr.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:instagram_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_insta.html",
        context=content
        )

def insta_sileme(request,id):
    sosyalmedyaInsgr.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:instagram_duzenleme_sayfasi")


def banner_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = banner_ekleme(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = banner.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:banner_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_banner.html",
        context=content
        )

def banner_sileme(request,id):
    banner.objects.filter(kategori_kime_ait = request.user,id = id).delete()
    return redirect("admin_panel:banner_duzenleme_sayfasi")

def hakkimizda_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = hakkimizda_ekleme(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = hakkimizda.objects.filter(kategori_kime_ait = request.user).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:hakkimizda_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_hakkimizda.html",
        context=content
        )

def bolgeler_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = bolgeler_ekleme(request.POST or None,request.FILES or None,user=request.user)
    content["form"] = logo_ekleme
    content["iconlar"] = bolgeler.objects.filter(kategori_kime_ait = request.user,silinme_bilgisi = False).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:bolgeler_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_bolgeler.html",
        context=content
        )
def bolgeler_sileme(request,id):
    bolgeler.objects.filter(kategori_kime_ait = request.user,id = id).update(silinme_bilgisi = True)
    return redirect("admin_panel:bolgeler_duzenleme_sayfasi")


def menu_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = menu_ekleme(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = menu.objects.filter(kategori_kime_ait = request.user,silinme_bilgisi = False).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:menu_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_menu.html",
        context=content
        )
def menu_sileme(request,id):
    menu.objects.filter(kategori_kime_ait = request.user,id = id).update(silinme_bilgisi = True)
    return redirect("admin_panel:menu_duzenleme_sayfasi")



def masa_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = masa_ekleme(request.POST or None,request.FILES or None,user=request.user)
    content["form"] = logo_ekleme
    content["iconlar"] = masalar.objects.filter(kategori_kime_ait = request.user,silinme_bilgisi = False).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:masa_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_masa.html",
        context=content
        )
def masa_sileme(request,id):
    masalar.objects.filter(kategori_kime_ait = request.user,id = id).update(silinme_bilgisi = True)
    return redirect("admin_panel:masa_duzenleme_sayfasi")

def kategori_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = kategori_ekleme(request.POST or None,request.FILES or None,user=request.user)
    content["form"] = logo_ekleme
    content["iconlar"] = kategoriler.objects.filter(kategori_kime_ait = request.user,silinme_bilgisi = False).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:kategori_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_kategoriler.html",
        context=content
        )
def kategori_sileme(request,id):
    kategoriler.objects.filter(kategori_kime_ait = request.user,id = id).update(silinme_bilgisi = True)
    return redirect("admin_panel:kategori_duzenleme_sayfasi")


def birim_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = birim_ekleme(request.POST or None,request.FILES or None)
    content["form"] = logo_ekleme
    content["iconlar"] = birimler.objects.filter(kategori_kime_ait = request.user,silinme_bilgisi = False).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:birim_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_birimler.html",
        context=content
        )
def birim_sileme(request,id):
    birimler.objects.filter(kategori_kime_ait = request.user,id = id).update(silinme_bilgisi = True)
    return redirect("admin_panel:birim_duzenleme_sayfasi")


def urun_duzenleme_sayfasi(request):
    content = site_bilgileri()
    logo_ekleme = urun_ekleme(request.POST or None,request.FILES or None,user=request.user)
    content["form"] = logo_ekleme
    content["iconlar"] = urunler.objects.filter(kategori_kime_ait = request.user,silinme_bilgisi = False).order_by("-id")
    if logo_ekleme.is_valid():

            profile = logo_ekleme.save(commit=False)
            profile.kategori_kime_ait = request.user
            profile.save()
            logo_ekleme.save_m2m()
            return redirect("admin_panel:urun_duzenleme_sayfasi")
    return render(
        request=request,
        template_name="admin_temp/admin_urun.html",
        context=content
        )
def urun_sileme(request,id):
    urunler.objects.filter(kategori_kime_ait = request.user,id = id).update(silinme_bilgisi = True)
    return redirect("admin_panel:urun_duzenleme_sayfasi")
