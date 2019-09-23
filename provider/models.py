from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=10, null=True)
    fax = models.CharField(max_length=10, null=True)
    toll_fee = models.CharField(max_length=10, blank=True, null=True, help_text='Contact phone number')
    email = models.EmailField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    user = models.ForeignKey(User, related_name='provider_user', on_delete=models.DO_NOTHING, null=True)


class Contact(models.Model):
    title = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=10, null=True)
    fax = models.CharField(max_length=10, null=True)
    toll_fee = models.CharField(max_length=10, blank=True, null=True, help_text='Contact phone number')
    email = models.EmailField(null=True)
    provider = models.ForeignKey(Provider, related_name='contact', on_delete=models.DO_NOTHING)


class Note(models.Model):
    note = models.TextField()
    created = models.DateField(auto_now=True)
    provider = models.ForeignKey(Provider, related_name='note', on_delete=models.DO_NOTHING)

