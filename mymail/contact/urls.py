from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
       path("contact", views.contact, name="contact"),
       path('thanks',views.thanks,name="thanks")   
]