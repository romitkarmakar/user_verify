from django.shortcuts import render
from .models import *
import json,math,random
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
# Create your views here.


def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(7) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 
def index(request):
    return render(request, 'index.html')

# def gen_otp(request):
#     if request.method == 'POST':
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         email= body["email"]
#         try:
#             user.objects.get(email=email)
#             return JsonResponse({'success': False,'error':"email already exists"})
#         except:
#             otp=generateOTP()
#             print(type(otp))
#             # user.objects.create(email=email,otp=otp)
#             return JsonResponse({'success': True,'otp':otp})

def verif_email(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        try:
            cur_user=user.objects.get(email=email)
            return JsonResponse({'success': True,'email_exists':True})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})

def ready_check(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        try:
            cur_user=user.objects.get(email=email)
            ready=cur_user.ready
            return JsonResponse({'ready_check':ready})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})


def user_data_entry(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user.objects.create(
        email= body["email"] ,
        first_name=body["first_name"],
        last_name=body["last_name"],
        date_of_birth=body["date_of_birth"],
        country_of_residence=body["country_of_residence"],
        state=body["first_name"],
        city_of_residence=body["city_of_residence"],
        phone_no=body["phone_no"],
        password=body["password"],
        fav_gnr_writing=body["fav_gnr_writing"],
        )
        return JsonResponse({'success': True})


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

def send_email(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        mail=body["email"]
        message=body["otp"]
        send_mail('sub',message ,settings.EMAIL_HOST_USER ,[mail])
        return JsonResponse({"success":True})
        

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return JsonResponse({"file_url":uploaded_file_url})
    return render(request, 'index.html')
