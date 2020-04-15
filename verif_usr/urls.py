from django.urls import path
from . import views

urlpatterns = [
    path('gen_otp',views.gen_otp, name="index"),
    path('verif_otp',views.verif_otp, name="verif_otp"),
    path('user_data_entry',views.user_data_entry, name="index"),
    path('verif_email_pswd',views.verif_email_pswd, name="index"),
]