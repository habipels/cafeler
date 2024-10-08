# Generated by Django 4.1.2 on 2024-04-28 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='kullanicilar_db',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lisans_bitis_tarihi',
            field=models.DateField(blank=True, null=True, verbose_name='Lisans Bitiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('yonetici', 'yonetici'), ('cafe_sahibi', 'cafe_sahibi'), ('mutfak', 'mutfak'), ('barista', 'barista'), ('cafe_kasa', 'cafe_kasa'), ('garson', 'garson'), ('', '')], default='', max_length=100),
        ),
    ]
