from django.shortcuts import render, HttpResponseRedirect
from loginsignup.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from loginsignup.decoraters import is_logged_in, logged_in_user_profile, is_registered


# create sign-up view
@is_registered
def signup_view(request):
    if request.method == "POST":
        fm = CustomUserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account created Successfully!")
            fm.save()
    else:
        fm = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': fm})


# login_view
@is_logged_in
def login_view(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
    else:
        fm = AuthenticationForm()
    return render(request, "userlogin.html", {'form': fm})


@logged_in_user_profile
def user_profile_view(request, *args, **kwargs):
    return render(request, "userprofile.html", {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/home/")
