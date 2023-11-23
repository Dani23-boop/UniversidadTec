from django.urls import path
from . import views
from .views import generar_reporte_pdf


urlpatterns = [
    path('', views.index),
    path('generar_reporte_pdf/', generar_reporte_pdf, name='generar_reporte_pdf'),   
]
