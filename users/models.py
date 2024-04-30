from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
# Create your models here.
class CustomUser(AbstractUser):

    STATUS = (
        ('yonetici', 'yonetici'),
        ('cafe_sahibi', 'cafe_sahibi'),
        ('mutfak','mutfak'),
        ('barista','barista'),
        ('cafe_kasa', 'cafe_kasa'),
        ('garson', 'garson'),
        ('', ''),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    lisans_bitis_tarihi = models.DateField(null=True,verbose_name="Lisans Bitiş Tarihi",blank = True)
    kullanicilar_db = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    def __str__(self):
        return self.username
