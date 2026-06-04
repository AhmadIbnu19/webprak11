from django.urls import path
from . import views

urlpatterns = [
    path("", views.halaman_grafik, name="halaman_grafik"),
    path("api/data-grafik/", views.data_grafik_api, name="data_grafik_api"),
    path("cetak/", views.halaman_cetak, name="halaman_cetak"),
    # URL untuk halaman utama PDF dan URL API static PDF-nya
    path("pdf-view/", views.halaman_utama_pdf, name="halaman_utama_pdf"),
    path("pdf-file/", views.buka_pdf, name="buka_pdf_file"),
]
