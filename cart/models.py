from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from shopping.models import *


# Create your models here.
class cartlist(models.Model):
    cartid=models.CharField(max_length=100,unique=True)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
  
    

class cartitem(models.Model):
 
    active=models.BooleanField(default=True)
    quantity=models.IntegerField()    
    product=models.ForeignKey(prducts,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    t = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status=models.CharField(max_length=50,default=1)
    cdate=models.DateTimeField(default='2023-10-30')
    def save(self, *args, **kwargs):
        # Call the 'total' method to calculate the total price (price * quantity)
        self.t = self.total()
        super(cartitem, self).save(*args, **kwargs)
    
    def total(self):
     
     return self.product.price*self.quantity
    

class checkout(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    towncity=models.CharField(max_length=100)
    postcodezip=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    checkoutdate=models.DateTimeField(default='2023-10-30')
    # status=models.IntegerField()

class payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    expiry_month=models.CharField(max_length=2)
    expiry_year=models.CharField(max_length=2)
    cvv=models.CharField(max_length=3)
    paymentdate=models.DateTimeField(default='2023-10-30')
    # status=models.IntegerField()

# class fcartdetails(models.Model):
#     cartid=models.ForeignKey(cartlist,on_delete=models.CASCADE)
#     total=models.CharField(max_length=255)
#     discount=models.CharField(max_length=255)
#     grandtotal=models.CharField(max_length=255)
#     cstatus=models.IntegerField()

    
      
   






