from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')
def intranet(request):
    return render(request, 'login/intranet.html')
