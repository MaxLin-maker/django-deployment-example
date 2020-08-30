from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from in_app import views

app_name='in_app'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('register/',views.register,name='register'),
    path('log_in/',views.log_in,name='log_in'),
    path('special/',views.special,name='special'),
    path('goodbye/',views.goodbye,name='goodbye'),
    path('log_out/',views.log_out,name='logout'),
]
