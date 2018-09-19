from django.shortcuts import render, redirect
from accounts.forms import \
    RegistrationForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash #this means that we still want to session to continue even though we change pass and redirect user
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
        return render(request, 'accounts/register.html', {'form': form}) #need a way to go back and poplulate the error on the form

    form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        return render(request, 'accounts/edit_profile.html', {'form': form})

    form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        return render(request, 'accounts/change_password.html', {'form': form})

    form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'accounts/change_password.html', args)


