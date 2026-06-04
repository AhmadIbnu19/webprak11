from django.shortcuts import render
from django.http import JsonResponse
from .models import PenjualanProduk
import os
from django.conf import settings
from django.http import FileResponse, Http404


# Create your views here.
def halaman_grafik(request):
    """View untuk merender halaman HTML utama"""
    return render(request, "core/grafik.html")


def data_grafik_api(request):
    """View API yang mengembalikan data dalam format JSON"""
    query_set = PenjualanProduk.objects.all()
    labels = []
    data = []

    for produk in query_set:
        labels.append(produk.nama_produk)
        data.append(produk.jumlah_terjual)

    return JsonResponse(
        {
            "labels": labels,
            "data": data,
        }
    )


def halaman_cetak(request):
    # Data contoh yang akan ditampilkan di dokumen
    konteks = {
        "nomor_invoice": "INV-2026-001",
        "nama_pelanggan": "Kadapi",
        "total_tagihan": "Rp 1.500.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000,00",
    }
    return render(request, "cetak_dokumen.html", konteks)


def buka_pdf(request):
    # Tentukan jalur ke file PDF Anda (misal di folder static)
    path_pdf = os.path.join(settings.BASE_DIR, "static", "dokumen", "sampel.pdf")

    if os.path.exists(path_pdf):
        # Buka file dalam mode binary read ('rb')
        file_pdf = open(path_pdf, "rb")
        # Kirim sebagai FileResponse agar dibuka di browser, bukan di-download
        return FileResponse(file_pdf, content_type="application/pdf")
    else:
        raise Http404("File PDF tidak ditemukan.")


def halaman_utama_pdf(request):
    return render(request, "lihat_pdf.html")
