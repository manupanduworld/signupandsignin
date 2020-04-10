from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import *


# Create your views here.
def signup(request):
    user_form = SignUpForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            # create profile for the user
            Profile.objects.create(user=new_user)
            profile_form = ProfileForm(instance=new_user.profile, data=request.POST)
            profile_form.save()

    context = {'user_form': user_form, "profile_form": profile_form}
    return render(request, 'authenticationapp/signup.html', context)

def signin(request):
    context = {}
    return render(request, 'authenticationapp/signin.html', context)