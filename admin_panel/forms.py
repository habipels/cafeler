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