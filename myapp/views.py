from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
from reportlab.pdfgen import canvas

def generar_reporte_pdf(request):
    # Crear un objeto HttpResponse con el tipo de contenido de PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el objeto PDF
    p = canvas.Canvas(response)

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 255)  # Color azul
    p.drawString(100, 800, "Hola, este es un reporte en PDF.")

    p.setFont("Helvetica-Bold", 16)  # Fuente en negrita
    p.setFillColorRGB(255, 0, 0)  # Color rojo
    p.drawString(100, 680, "Diplomas.")

    p.setFont("Helvetica-Oblique", 14)  # Fuente en cursiva
    p.setFillColorRGB(0, 128, 0)  # Color verde
    p.drawString(100, 580, "Nombre del taller.")

    p.setFont("Helvetica", 12)  # Restablecer la fuente
    p.setFillColorRGB(0, 0, 0)  # Restablecer el color
    p.drawString(100, 780, "Nombre del Participante.")



    # Cerrar el objeto PDF y finalizar la respuesta
    p.showPage()
    p.save()

    return response

def index(request):
    return render(request, 'index.html')
