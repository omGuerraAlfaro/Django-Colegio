from django.shortcuts import redirect, render
from oauth_app.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def LoginGoogle(request):
    return render(request, 'oauth_app/loginGoogle.html')

def add_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oauth_app/loginGoogle')
            
    else:
        form = SignUpForm()
    return render(request, 'inicio/index.html', {'form': form})