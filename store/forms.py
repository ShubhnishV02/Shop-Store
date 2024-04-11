from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bord1','placeholder':'Username','required':'True'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bord3','placeholder':'name@example.com','required':'True'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bord3','placeholder':'Password','required':'True', 'type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bord2','placeholder':'Confirm Password','required':'True', 'type':'password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']