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
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number', default='000000000')
    fax = PhoneField(blank=True, null=True, help_text='Contact phone number', default='000000000')
    toll_free = PhoneField(blank=True, null=True, help_text='Contact phone number')
    email = models.EmailField(max_length=50, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='provider_user', on_delete=models.DO_NOTHING)


class Contact(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    fax = PhoneField(blank=True, null=True, help_text='Contact phone number')
    toll_free = PhoneField(blank=True, null=True, help_text='Contact phone number')
    email = models.EmailField(max_length=50, blank=True, null=True)
    provider = models.ForeignKey(Provider, related_name='contact', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name='contact_user', on_delete=models.DO_NOTHING)

class Note(models.Model):
    note = models.TextField()
    created = models.DateField(auto_now=True)
    provider = models.ForeignKey(Provider, related_name='note', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name='note_user', on_delete=models.DO_NOTHING)
