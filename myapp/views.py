from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('landing'))  # Replace 'landing' with your landing page URL name
        else:
            error_message = 'Incorrect credentials'
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html', {'error': ''})


def landing_view(request):
    user = request.user
    return render(request, 'landing.html', {'username': user.username})
