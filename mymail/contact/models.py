from django.db import models
from django.forms import ModelForm






class Country(models.Model):
   name = models.CharField(max_length=30)

   def __str__(self):
        return self.name



class Contact(models.Model):
    name =  models.CharField(max_length=50)
    email = models.EmailField()
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=11) 
    mobile = models.CharField(max_length=11) 
    message = models.TextField(default='')
    country = models.ForeignKey(Country, on_delete= models.CASCADE)

    

