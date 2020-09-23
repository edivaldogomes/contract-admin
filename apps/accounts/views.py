from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from apps.accounts import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
    # Return an 'invalid login' error message.
            messages.error(request, 'Entra o nome e palavra-passe correcta!',
                           extra_tags='alert alert-danger alert-dismissible fade show')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')

@login_required(login_url='/accounts/login/')
def user_registration(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            messages.success(request, 'Obrigado por te registares {}'.format(user.username),
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('home')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='/accounts/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            return redirect('accounts:cambiar_contaseña')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/cambiar_contrasenna.html', args)