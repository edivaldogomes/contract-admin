from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Nome de usuario', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuario'}))
    first_name = forms.CharField(label='Nome', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    last_name = forms.CharField(label='Sobrenome', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@exemplo.com'}))
    password1 = forms.CharField(label='Palavra-passe', max_length=100, min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar palavra-passe', max_length=100, min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('O nome do usuario ja existe, escolhe otro por favor')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('O email ja existe actualmente')
        return email

    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 != p2:
            raise ValidationError('A palavra-passe não coincide com a posta anteriormente')
        return p1
