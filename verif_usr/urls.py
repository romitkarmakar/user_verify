from django.urls import path
from . import views

urlpatterns = [
    # path('gen_otp',views.gen_otp, name="index"),
    path('verif_email',views.verif_email, name="verif_otp"),
    path('user_data_entry',views.user_data_entry, name="index"),
    path('verif_email_pswd',views.verif_email_pswd, name="index"),
    path("index",views.index,name="index"),
    path("upload",views.upload,name="upload"),
    path("send_mail",views.send_email,name="send_mail"),
    path("ready_check",views.ready_check,name="send_mail"),
]