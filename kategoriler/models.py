from django.db import models
from ckeditor.fields import RichTextField
from users.models import *
# Create your models here.
class kategory_link_ayari(models.CharField):
    def __init__(self, *args, **kwargs):
        super(kategory_link_ayari, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).lower().replace(" ","_")

class kategoriler(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    isim = models.CharField(max_length=50)
    link = kategory_link_ayari(max_length=100 , null="True")
    keywords = models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    def __str__(self):
        full_path = [self.isim]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.isim)
            k = k.parent
        return ' --> '.join(full_path[::-1])

class urunler(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    siralama = models.BigIntegerField(null=True)
    category = models.ForeignKey(kategoriler, on_delete=models.CASCADE)
    isim = models.CharField(max_length=150)
    link = kategory_link_ayari(max_length=100 , null="True")
    keywords = models.CharField(max_length=255)
    resimi=models.ImageField(upload_to='images/',null=False)
    fiyat = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    Durum=models.CharField(max_length=10,choices=STATUS,default = "Evet")
    create_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.isim


# Create your models here.
class sayfa_logosu(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sayfa_logo = models.FileField(upload_to='logo/',blank = True,null = True,verbose_name="Sayfaya Logo Ekleyin")
class sayfa_iconu(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sayfa_logo = models.FileField(upload_to='icon/',blank = True,null = True,verbose_name="Sayfaya icon Ekleyin")
class site_adi(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    site_adi_genel = models.CharField(max_length=200)
    def __str__(self):
        return self.site_adi_genel
class numara(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sirket_numarasi = models.CharField(max_length=11)
    def __str__(self):
        return self.sirket_numarasi
class adres(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sirket_adresi = models.CharField(max_length=200)
    def __str__(self):
        return self.sirket_adresi
class email_adres(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sirket_email_adresi = models.EmailField(max_length=200)
    def __str__(self):
        return self.sirket_email_adresi
class sosyalmedyaTw(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    link = models.CharField(max_length=400)
    def __str__(self):
        return self.link
class sosyalmedyafb(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    link = models.CharField(max_length=400)
    def __str__(self):
        return self.link
class sosyalmedyaInsgr(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    link = models.CharField(max_length=400)
    def __str__(self):
        return self.link
class banner(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sayfa_sirasi = models.BigIntegerField(null=True)
    baner_resim = models.FileField(upload_to='banner/',blank = True,verbose_name="Sayfaya resim Ekleyiniz")

from ckeditor.fields import RichTextField
class hakkimizda(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    hakkimda = RichTextField()
class iletisim(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    iletisim_yollari = RichTextField()

class cafe_resmi (models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    resim = models.FileField(upload_to='kafe/',blank = True,verbose_name="Sayfaya resim Ekleyiniz")

class aciklama(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    footer_aciklama= models.TextField()
    def __str__(self):
        return self.footer_aciklama

class sekme_icon (models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    resim = models.FileField(upload_to='icon/',blank = True,verbose_name="sekmeye resim Ekleyiniz")
