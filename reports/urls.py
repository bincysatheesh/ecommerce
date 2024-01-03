from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    
    path('generate_invoice_pdf/<int:payment_id>/', views.generate_invoice_pdf, name='generate_invoice_pdf'),
]
