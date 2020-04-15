from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=128,blank=True)
    last_name=models.CharField(max_length=128,blank=True)
    date_of_birth=models.CharField(max_length=128,blank=True)
    country_of_residence=models.CharField(max_length=128)
    state=models.CharField(max_length=128)
    city_of_residence=models.CharField(max_length=128)
    phone_no=models.CharField(max_length=15)
    fav_gnr_writing=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    password=models.CharField(max_length=30,default="")
    ready=models.BooleanField(default=False)
