from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import *
from shopping.models import *
from accounts.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# # session

# def c_id(request):
#     ct_id=request.session.session_key # Try to retrieve the ct_id from the session
#     if not ct_id:
#         ct_id=request.create()
#     return ct_id
def loadpayment(request):

    return render(request,'bankdetails.html')




 