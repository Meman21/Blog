from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2',]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['image']

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class   ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    message= forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    forcefield =forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leavae empty", validators=[should_be_empty])




    



    
