from django.db import models


class Calisan(models.Model):
    calisanNo = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    cinsiyet = models.CharField(max_length=1)
    gorev = models.CharField(max_length=100)
    calisanTipi = models.CharField(max_length=100)

    class Meta:
        db_table = "Calisan"
