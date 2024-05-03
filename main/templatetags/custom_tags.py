from django import template 
from django.utils.safestring import mark_safe
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect

register = template.Library()
#@register.filter
#@register.simple_tag
