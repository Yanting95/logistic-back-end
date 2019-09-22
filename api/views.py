from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from provider.models import Provider
from api.serializers import ProviderSerializer, UserSerializer


@api_view(['GET', 'POST'])
def provider_list(request):

    if request.method == 'GET':
        provider = Provider.objects.all()
        serializer = ProviderSerializer(provider, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_detail(request, pk):

    try:
        provider = Provider.objects.get(pk=pk)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        provider_detail = Provider.objects.get(pk=pk)
        serializer = ProviderSerializer(provider_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data,
                     'token': token.key},
                    status=HTTP_200_OK)
