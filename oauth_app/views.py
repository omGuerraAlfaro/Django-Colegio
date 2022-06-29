from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

def LoginGoogle(request):
    v_user =  request.POST.get('emailInicio')
    v_pass = request.POST.get('passInicio')
    try:
        usuario = User.objects.get(username=v_user)
    except User.DoesNotExist:
        return render(request, 'oauth_app/loginGoogle.html')
    pass_valido = check_password(v_pass, usuario.password)    
    if not pass_valido:
        return render('oauth_app/loginGoogle.html')
    token, created = Token.objects.get_or_create(user=usuario)
    return render('oauth_app/loginGoogle.html')
