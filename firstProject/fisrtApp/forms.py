from django import forms  
from fisrtApp.models import Product
from django.forms import fields
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User  # Specify the User model
        fields = ['username', 'email', 'password']

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = "__all__"  