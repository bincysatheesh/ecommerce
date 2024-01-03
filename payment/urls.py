from django.urls import path,include
from .import views
urlpatterns = [  
    path('loadpayment',views.loadpayment,name='loadpayment'),
    # path('add/<int:pid>/',views.addt,name='addrt'),
   
   
]
