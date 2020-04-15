from django.shortcuts import render
from .models import *
import json,math,random
from django.http import JsonResponse
# Create your views here.

def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(7) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 

def gen_otp(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        try:
            user.objects.get(email=email)
            return JsonResponse({'success': False,'error':"email already exists"})
        except:
            otp=generateOTP()
            print(type(otp))
            # user.objects.create(email=email,otp=otp)
            return JsonResponse({'success': True,'otp':otp})

def verif_otp(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        otp=body["otp"]
        try:
            cur_user=user.objects.get(email=email)
            if cur_user.otp==int(otp):
                return JsonResponse({'success': True,'verified':True})
            else:
                return JsonResponse({'success': False,'verified':False})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})


def user_data_entry(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        try:
            cur_user=user.objects.get(email=email)
            cur_user.first_name=body["first_name"]
            cur_user.last_name=body["last_name"]
            cur_user.date_of_birth=body["date_of_birth"]
            cur_user.country_of_residence=body["country_of_residence"]
            cur_user.state=body["first_name"]
            cur_user.city_of_residence=body["city_of_residence"]
            cur_user.phone_no=body["phone_no"]
            cur_user.password=body["password"]
            cur_user.fav_gnr_writing=body["fav_gnr_writing"]
            cur_user.ready=body["ready"]
            cur_user.save()
            return JsonResponse({'success': True})

        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})


def verif_email_pswd(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        password= body["password"]
        try:
            cur_user=user.objects.get(email=email)
            if cur_user.password==password:
                return JsonResponse({'success': True,'verified':True})
            else:
                return JsonResponse({'success': False,'verified':False,'error':"wrong password"})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})

