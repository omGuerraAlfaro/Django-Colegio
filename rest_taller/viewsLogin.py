from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def loginApi(request):
    data = JSONParser().parse(request)
    v_user = data['username']
    v_pass = data['password']
    try:
        usuario = User.objects.get(username=v_user)
    except User.DoesNotExist:
        return Response("Usuario invalido")
    pass_valido = check_password(v_pass, usuario.password)    
    if not pass_valido:
        return Response("Password incorrecta")
    token, created = Token.objects.get_or_create(user=usuario)
    return Response(token.key)
