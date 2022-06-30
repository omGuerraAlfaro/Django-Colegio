from django.shortcuts import render

def LoginGoogle(request):
    return render(request, 'oauth_app/loginGoogle.html')

