# Register your models here.
from django.contrib import admin
from .models import Contact,Country

admin.site.register(Country)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display =['id','name','email','company','designation','mobile','message']
















