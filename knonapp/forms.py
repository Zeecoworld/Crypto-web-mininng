from django import forms
from .models import Newsletter



class NewsletterForm(forms.ModelForm):

    class Meta:
            model = Newsletter
            fields = ['email',]
            widgets = {
                'email': forms.EmailInput(attrs={'type':'text','placeholder':'Enter your email'}),
            }
