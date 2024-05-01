from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from kategoriler.models import *
from django.forms import ModelForm

class logo_ekle(ModelForm):
    class Meta:
        model = sayfa_logosu
        fields = [
            'sayfa_logo'
        ]

class icon(ModelForm):
    class Meta:
        model = sayfa_iconu
        fields = [
            'sayfa_logo'
        ]

class site_isimleri(ModelForm):
    class Meta:
        model = site_adi
        fields = [
            'site_adi_genel',
            'site_url_ayari'
        ]
class isletmenumarasi(ModelForm):
    class Meta:
        model = numara
        fields = [
            'sirket_numarasi'
        ]
class adresi(ModelForm):
    class Meta:
        model = adres
        fields = [
            'sirket_adresi'
        ]

class eposta(ModelForm):
    class Meta:
        model = email_adres
        fields = [
            'sirket_email_adresi'
        ]
#