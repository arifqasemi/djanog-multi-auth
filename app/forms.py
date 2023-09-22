from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, Admin,User

class CustomerSignUpForm(UserCreationForm):
    username=forms.CharField(required=False)
    email=forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.email = self.cleaned_data['email'] 
        user.save()
        student = Customer.objects.create(user=user)
        return user
    
class ManagerSignUpForm(UserCreationForm):
    username=forms.CharField(required=True)
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_admin = True
        user.email = self.cleaned_data['email'] 
        user.save()
        manager = Admin.objects.create(user=user)
        manager.save()

        return manager
  

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=254, error_messages={'required': 'email is required'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': 'Password is required'})

    class Meta:
        model = User
        fields = ("email", "password")
