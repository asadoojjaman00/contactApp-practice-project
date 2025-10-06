from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company')
    search_fields = ('name','email', 'phone', 'company')