from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .models import Contact

def thanks(request):
   return render(request,"contact/thanks.html")
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()
            subject = 'hello yagnesh'
            #import pdb;pdb.set_trace() 
            body = {
            'name': form.cleaned_data['name'], 
            'email': form.cleaned_data['email'], 
            'company': form.cleaned_data['company'], 
            'designation':form.cleaned_data['designation'],
            'mobile': form.cleaned_data['mobile'], 
            'message': form.cleaned_data['message'],
          
            'country': str(form.cleaned_data['country']), #conver in to string for use object for foreginkey 
             }
            #print(body["country"])
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, '', ['']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("thanks")
    form = ContactForm()

    return render(request, "contact/contact.html", {'form':form})
