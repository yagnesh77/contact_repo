from django import forms
from . import models
from django.forms import ModelForm





class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
      

