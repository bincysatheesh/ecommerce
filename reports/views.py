from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from cart.models import payment  # Import the Payment model
from reportlab.pdfgen import canvas

def generate_invoice_pdf(request, payment_id):
    # Retrieve payment details based on the payment_id
    payment_obj = payment.objects.get(id=payment_id)
    
    # Create the response as a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=invoice_{payment_id}.pdf'

    # Create the PDF document using ReportLab
    p = canvas.Canvas(response)

    # Add content to the PDF, e.g., payment details
    p.drawString(100, 750, f'Invoice ID: {payment_obj.id}')
    p.drawString(100, 730, f'Date: {payment_obj.paymentdate}')
    p.drawString(100, 710, f'Account Number: {payment_obj.account_number}')
    p.drawString(100, 690, f'Name: {payment_obj.name}')
    p.drawString(100, 670, f'Expiry Month: {payment_obj.expiry_month}')
    p.drawString(100, 650, f'Expiry Year: {payment_obj.expiry_year}')

    # Finish the PDF and return the response
    p.showPage()
    p.save()

    return response
