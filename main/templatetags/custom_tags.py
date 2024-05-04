from django import template 
from django.utils.safestring import mark_safe
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from kategoriler.models import *
register = template.Library()
#@register.filter
#@register.simple_tag
@register.simple_tag
def masa_sayisi(id):
    #sayi = masalar.objects.filter(bolge_isimi = id).count()
    return id
    