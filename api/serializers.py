from rest_framework import serializers
from django.contrib.auth.models import User
from provider.models import Provider, Contact, Note


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'address', 'country', 'city', 'state', 'zip',
                  'phone', 'fax', 'toll_fee', 'email', 'start_time', 'end_time', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('title', 'first_name', 'last_name', 'mobile', 'phone', 'fax', 'toll_fee', 'email')


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('note', 'created', 'provider')
