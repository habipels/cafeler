from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from kategoriler.models import *
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django.forms import CharField
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

class insta(ModelForm):
    class Meta:
        model = sosyalmedyaInsgr
        fields = [
            'link'
        ]
class banner_ekleme(ModelForm):
    class Meta:
        model = banner
        fields = [
            'sayfa_sirasi',
            'baner_resim'
        ]
#
class hakkimizda_ekleme(ModelForm):
    hakkimda = CharField(widget=CKEditorWidget(attrs={'class': 'form-control'}),label="Hakkımızda ",
        required=False)
    class Meta:
        model = hakkimizda
        fields = [
            'hakkimda'
        ]
    


class bolgeler_ekleme(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(bolgeler_ekleme, self).__init__(*args, **kwargs)
        self.fields['bolge_menu'].queryset = menu.objects.filter(kategori_kime_ait=user)

    class Meta:
        model = bolgeler
        fields = ['bolge_menu', 'bolge_isimi']

class menu_ekleme(forms.ModelForm):
    class Meta:
        model = menu
        fields = ['menu_isimi']
class masa_ekleme(ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(bolgeler_ekleme, self).__init__(*args, **kwargs)
        self.fields['bolge_isimi'].queryset = bolgeler.objects.filter(kategori_kime_ait=user)
    class Meta:
        model = masalar
        fields = [ 
            'bolge_isimi',
            "masa_isimi"
        ]


class kategori_ekleme(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(kategori_ekleme, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = kategoriler.objects.filter(kategori_kime_ait=user)

    class Meta:
        model = kategoriler
        fields = ['isim', 'parent',"Durum"]
