from rest_framework import serializers
from django.contrib.auth.models import User
from provider.models import Provider


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'address', 'country', 'city', 'state', 'zip',
                  'phone', 'fax', 'email', 'start_time', 'end_time', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')