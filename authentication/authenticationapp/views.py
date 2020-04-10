from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.
def signup(request):
    form = SignUpForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = SignUpForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'authenticationapp/signup.html', context)
def signin(request):
    context = {}
    return render(request, 'authenticationapp/signin.html', context)