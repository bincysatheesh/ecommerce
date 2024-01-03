from django.urls import path,include
from .import views
urlpatterns = [  
    path('loadcart',views.loadcart,name='loadcart'),
    path('add/<int:pid>/',views.addcart,name='addcart'),
    path('min_cart/<int:pid>/', views.min_cart, name='min_cart'),
    path('cart_delete/<int:pid>/', views.cart_delete, name='cart_delete'),
    path('checkout', views.checkoutview, name='checkout'),
    path('payment', views.paymentview, name='payment'),
    path('cart/thankyou/', views.thankyou, name='thankyou'),
    # path("razorpay_payment", views.razorpay_payment, name="razorpay_payment"),


   
]
