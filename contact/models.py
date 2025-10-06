from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    company = models.CharField(max_length=90)
    

    def __str__(self):
        return self.name