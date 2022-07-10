from ssl import AlertDescription
from tabnanny import check
from django.shortcuts import render,redirect
from urllib import request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login

@api_view(['POST'])
def loginApi(request):
    
    username = request.data['username']
    password = request.data['password']

    try:
        user = User.objects.get(email = username)
    except User.DoesNotExist:
        return redirect("loginGoogle")

    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return redirect("loginGoogle")

    token, created = Token.objects.get_or_create(user=user)
    login(request,user)
    return redirect("index") #return Response(token.key)