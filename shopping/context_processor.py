from .views import *
from django.core.exceptions import ObjectDoesNotExist
from cart.models import *



def categ(request):
    obj=category.objects.all()
    return {'d':obj}   


def cart_context(request):
    t = 0
    cn = 0
    dt = 0
    da = 0
 

    try:
        user = request.user
        if user.is_authenticated:
            ct = cartlist.objects.filter(user=user)
        else:
            cart_id = request.session.get('cartid')
            ct = cartlist.objects.filter(cartid=cart_id)

        ct_items = cartitem.objects.filter(cart__in=ct, active=True)

        for i in ct_items:
            t += i.product.price * i.quantity
            cn += i.quantity

        dt = 10000

        if t > dt:
            dp = 10
            damount = (t * dp) / 100
            dtotal = (t - damount)*100
            dr=dtotal/100
        else:
            damount = 0
            dtotal = t*100
            dr=dtotal/100

    except ObjectDoesNotExist:
        pass

    
    return {'t': t,'cn': cn,'dt': dtotal,'dr':dr,'da': damount}


              
