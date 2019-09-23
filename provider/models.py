from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=5)
    phone = PhoneField(blank=True, help_text='Contact phone number', default='000000000')
    fax = PhoneField(blank=True, help_text='Contact phone number', default='000000000')
    email = models.EmailField(max_length=50)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    user = models.ForeignKey(User, related_name='provider_user', on_delete=models.DO_NOTHING, null=True)


class Contact(models.Model):
    title = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = PhoneField(blank=True, help_text='Contact phone number')
    office_phone = PhoneField(blank=True, help_text='Contact phone number')
    fax_number = PhoneField(blank=True, help_text='Contact phone number')
    toll_fee = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=50)
    provider = models.ForeignKey(Provider, related_name='contact', on_delete=models.DO_NOTHING, null=True)



