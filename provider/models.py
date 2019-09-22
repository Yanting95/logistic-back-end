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
    email = models.EmailField(max_length=50)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    user = models.ForeignKey(User, related_name='provider_user', on_delete=models.DO_NOTHING, null=True)
