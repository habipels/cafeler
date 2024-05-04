from django.db import models
from ckeditor.fields import RichTextField
from users.models import *
import qrcode

# Create your models here.
class kategory_link_ayari(models.CharField):
    def __init__(self, *args, **kwargs):
        super(kategory_link_ayari, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).lower().replace(" ","_")

class kategoriler(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    isim = models.CharField(max_length=150,verbose_name="Adı")
    link = kategory_link_ayari(max_length=100 , null="True")
    keywords = models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    Durum=models.CharField(max_length=10,verbose_name="Menüde Göster",choices=STATUS,default = "Evet")
    parent = models.ForeignKey('self',verbose_name="Üst Kategorisi Var Mı ? ",blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    silinme_bilgisi = models.BooleanField(default=False,verbose_name="Silinme Bilgisi")
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
    siralama = models.BigIntegerField(null=True,verbose_name="Sıralaması")
    category = models.ForeignKey(kategoriler,verbose_name="Kategorisi", on_delete=models.CASCADE)
    isim = models.CharField(max_length=150,verbose_name="İsmi")
    link = kategory_link_ayari(max_length=100 , null="True",verbose_name="Tanıtım Açıklaması")
    keywords = models.CharField(max_length=255)
    resimi=models.ImageField(upload_to='images/',null=False)
    fiyat = models.DecimalField(max_digits=12, decimal_places=2,default=0,verbose_name="Fiyatı")
    Durum=models.CharField(max_length=10,verbose_name="Menüde Göster",choices=STATUS,default = "Evet")
    create_at=models.DateTimeField(auto_now_add=True)
    silinme_bilgisi = models.BooleanField(default=False,verbose_name="Silinme Bilgisi")
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
    site_adi_genel = models.CharField(max_length=200,verbose_name="İşletme Adı")
    site_url_ayari =kategory_link_ayari(max_length=100 ,verbose_name="İşletme Adı")
    def __str__(self):
        return self.site_adi_genel
class numara(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    sirket_numarasi = models.CharField(max_length=11,verbose_name="İşletme Numarası (0555555555)")
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
    link = models.CharField(max_length=400,verbose_name="İnstagram Adres Linki")
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
class menu(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    menu_isimi = models.CharField(max_length=200,verbose_name="Menü Adı")
    silinme_bilgisi = models.BooleanField(default= False,verbose_name="Silinme Bilgisi")
    def __str__(self) -> str:
        if self.silinme_bilgisi:
            return  "Silinen Menü : "+self.menu_isimi
        else:
            return self.menu_isimi
class bolgeler(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    bolge_menu = models.ForeignKey(menu,verbose_name="Menü ",blank=True,null=True,on_delete=models.CASCADE)
    bolge_isimi = models.CharField(max_length=200,verbose_name="Bölge Adı")
    silinme_bilgisi = models.BooleanField(default= False,verbose_name="Silinme Bilgisi")
    def __str__(self) -> str:
        if self.silinme_bilgisi:
            return  "Silinen"+self.bolge_isimi
        else:
            return self.bolge_isimi
from PIL import Image
from io import BytesIO
import qrcode

class masalar(models.Model):
    kategori_kime_ait = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    bolge_isimi = models.ForeignKey(bolgeler,verbose_name="Bölge ",blank=True,null=True,on_delete=models.CASCADE)
    masa_isimi =models.CharField(max_length= 200,verbose_name="Masa Adı")
    image = models.ImageField(upload_to='qr/',blank=True,null=True,verbose_name="Masa Qrları")
    silinme_bilgisi = models.BooleanField(default=False,verbose_name="Silinme Bilgisi")

    def save(self, *args, **kwargs):
        if not self.pk:  # Eğer bu nesne henüz kaydedilmediyse (yani yeni bir nesne oluşturuluyorsa)
            data = f"https://example.com/detail/{self.id}/"
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = BytesIO()
            img.save(buffer, format='PNG')  # PNG formatında kaydetmek
            buffer.seek(0)
            self.image.save(f'qr_code_{self.id}.png', buffer, save=False)  # QR kodunu kaydet

        super().save(*args, **kwargs)

    
    