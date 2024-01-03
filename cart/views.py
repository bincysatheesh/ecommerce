from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import *
from shopping.models import *
from accounts.models import *
from cart.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import razorpay
from datetime import datetime

# session

def c_id(request):
    ct_id=request.session.session_key # Try to retrieve the ct_id from the session
    if not ct_id:
         ct_id=request.create()
        # request.session.create()
        # ct_id = request.session.session_key
    return ct_id

# decorator
@login_required(login_url='loadregister')
def addcart(request,pid):
    prod=prducts.objects.get(id=pid)
    user=request.user
    try:
        ct=cartlist.objects.get(user=user)
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cartid=c_id(request),user=user)
        ct.save()
    try:
        current_date = datetime.now()
        c_items=cartitem.objects.get(product=prod,cart=ct)
        # print(c_items)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
            prod.stock-=1
            prod.save()
        # ct.status = "carted"   
        c_items.save()    
    except cartitem.DoesNotExist:
        c_items=cartitem.objects.create(product=prod,quantity=1,cart=ct,cdate=current_date)
        prod.stock-=1
        prod.save()
        c_items.save()    
    return redirect('loadcart')

dp = 5
def loadcart(request,tot=0,count=0,cart_items=None,ct_items=None):
    try:
        user= request.user
        if user.is_authenticated:
            ct=cartlist.objects.filter(user=user)
        else:
            cart_id=request.session.get('cartid')
            ct=cartlist.objects.filter(cartid=cart_id)
        # --------------------------------
        ct_items=cartitem.objects.filter(cart__in=ct,active=True)

        # it=[]
        # for j in ct_items:
        #     it=(j.product.price*j.quantity)
        #     it.append(it)
        


        for i in ct_items:
        # Calculate the total amount and total quantity
            tot+=(i.product.price * i.quantity)
            count+=i.quantity
# ***********************************************************************************
        #  # Calculate the discount amount
        # damount = (tot * dp) / 100

        # # Apply the discount to the total
        # dtotal = tot - damount
# ***********************************************************************************
   
        dt = 10000

        if tot > dt:
            dp = 10  
            damount = (tot * dp) / 100

            # Apply the discount to the total
            dtotal = (tot - damount)*100
            dtr = dtotal / 100
        else:
            damount = 0
            dtotal = (tot- damount)*100
            dtr = dtotal / 100
# ----------------------------------------------------------------------
        ct.gt = dtr

  # Update the cartlist with the calculated grand total and discount
        # ct = ct.first()  # Retrieve the first cartlist
        # ct.gt = dtr  # Set the grand total to dtotal
        # ct.discount = damount  # Set the discount to damount
        # ct.save()
        ct = ct.first()  # Retrieve the first cartlist
        if ct is not None:
         ct.gt = dtr  # Set the grand total to dtr
         ct.discount = damount  # Set the discount to damount
         ct.save()

# ***********************************************************************************

    except ObjectDoesNotExist:
        return HttpResponse("<script> alert('Empty Cart');window.location='/';<script>")
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count,'dt':dtotal,'dtr':dtr,'da':damount})


   


# ---------------------------------
@login_required(login_url='loadregister')
def min_cart(request,pid):
    user=request.user
    try:
        if user.is_authenticated:
            ct_list=cartlist.objects.filter(user=user)
        else:
            cart_id=request.session.get('cartid')
            ct_list=cartlist.objects.filter(cart_id=cart_id)
        if ct_list.exists:
            for ct in ct_list:
                prod=get_object_or_404(prducts,id=pid)
                try:
                    c_items=cartitem.objects.get(product=prod,cart=ct)
                    if c_items.quantity>1:
                        c_items.quantity-=1
                        prod.stock+=1
                        prod.save()
                        c_items.save()
                    else:
                        c_items.delete()
                except cartitem.DoesNotExist:
                    pass
    except cartlist.DoesNotExist:
        pass

    return redirect('loadcart')
# ========================================


@login_required(login_url='loadregister')
def cart_delete(request,pid):
    user=request.user
    try:
        if user.is_authenticated:
            ct_list=cartlist.objects.filter(user=user)
        else:
            cart_id=request.session.get('cartid')
            ct_list=cartlist.objects.filter(cart_id=cart_id)
        if ct_list.exists:
            for ct in ct_list:
                prod=get_object_or_404(prducts,id=pid)
                try:
                    c_items=cartitem.objects.get(product=prod,cart=ct)
                    c_items.delete()
                except cartitem.DoesNotExist:
                    pass
    except cartlist.DoesNotExist:
        pass
    return redirect('loadcart')


def checkoutview(request,cn=0,da=0,dt=0,dr=0,t=0):
  

    if request.method=="POST":
        # print("hai?*****************************************************")
        fn=request.POST['fname']
        ln=request.POST['lname']
        country=request.POST['country']
        address=request.POST['address']
        towncity=request.POST['town']
        zipcode=request.POST['zipcode']
        phone=request.POST['phone']
        email=request.POST['email']
        # first()-recent data which has enter to table
        cart = cartlist.objects.filter(user=request.user).first()
        # cart =c_id(request)
        # print(cart)
        if cart:
            print("hello")
            if 'cn' in request.GET:
                cn = request.GET['cn']
                # print("hiiiiiiiiiiii")
            if 'da' in request.GET:
                da = request.GET['da']
            if 'dt' in request.GET:
                dt = request.GET['dt']
            if 'dr' in request.GET:
                dr = request.GET['dr']
            if 't' in request.GET:
                t = request.GET['t']
            current_date = datetime.now()
            checkout_data = checkout(user=request.user,cart=cart,firstname=fn,lastname=ln,country=country,address=address,towncity=towncity,postcodezip=zipcode,phone=phone,email=email,checkoutdate=current_date)    
            checkout_data.save()
        # if not cart:
        #     #  the cart does not exist
        #     return HttpResponse("<script> alert('Empty Cart');window.location='/';</script>")

        # # Get the specific cart item for the product
        # cart_item = cartitem.objects.get(cart=cart)
        
        # if cart_item.status == 'checkout completed':
        #     # Handle the case where the item is already checked out
        #     return HttpResponse("<script> alert('Item is already checked out');window.location='/';</script>")
        
        # # Update the status of the specific cart item
        # cart_item = cartitem.objects.get(cart_id=cart)        
        # cart_item.status = 'checkout completed'
        # cart_item.save()
        cart_items = cartitem.objects.filter(cart__user=request.user)
        for item in cart_items:
        # Update the status of each cart item to 'checkout completed'
            item.status = 'checkout completed'
            item.save()
        
        print("Your data SAVED successfullty...")
        return render(request, 'payment.html', {'cn': cn, 'da': da, 'dt': dt,'dr':dr, 't': t})
        
       
    return render(request, 'checkout.html')

def paymentview(request):
    if request.method=="POST":
        # print("hai?*****************************************************")
        acn=request.POST['acn']
        name=request.POST['name']
        em=request.POST['em']
        ey=request.POST['ey']
        cvv=request.POST['cvv']
        # status=1
        current_date = datetime.now()
        payment_data = payment(user=request.user,account_number=acn,name=name,expiry_month=em,expiry_year=ey,cvv=cvv,paymentdate=current_date)    
        payment_data.save()    
      # Update the status of cartitem to "payment finished"
        user = request.user
        ct = cartlist.objects.get(user=user)
        cart_items = cartitem.objects.filter(cart=ct)
        for cart_item in cart_items:
            cart_item.status = "payment finished"
            cart_item.active = False  # Deactivate the cart item
            cart_item.save()  # Save each cart item

       

        # user = request.user
        # ct = cartlist.objects.get(user=user)
        # cartitem.objects.filter(cart=ct).delete()
        print("Your Payment has done successfullty...")
        return redirect("/")
        
       
    return render(request, 'payment.html')



def thankyou(request):
    return render(request, 'thankyou.html')




























 # # decrease the stock level ...when an item add to the cart
            # product=i.product
            # if product.stock>=i.quantity:
            #     product.stock-=i.quantity
            #     product.save()
            # else:
            #      return HttpResponse("<script> alert('Not enough stock for some items in your cart!!!!');window.location='/';<script>")
   