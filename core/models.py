from django.db import models


# Create your models here.
class PenjualanProduk(models.Model):
    nama_produk = models.CharField(max_length=100)
    jumlah_terjual = models.IntegerField()

    def __str__(self):
        return f"{self.nama_produk} ({self.jumlah_terjual})"
