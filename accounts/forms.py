from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class MyUserCreationForm(UserCreationForm):


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'type':'text',
            'placeholder':'Enter your username'
        })
        self.fields["email"].widget.attrs.update({
            'type':'email',
            'placeholder':'Enter your email'
        })
        self.fields["password1"].widget.attrs.update({
            'type':'password',
            'placeholder':'Enter your password'
        })
        self.fields["password2"].widget.attrs.update({
            'type':'password',
            'placeholder':'Confirm your password'
        })


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

  
