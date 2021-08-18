from django import forms
from django.forms import ModelForm
from .models import contact



class ContactForm(ModelForm):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Name', "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email',  'class': 'form-control'}))
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Message', "class": "form-control"}))
    message = forms.CharField( max_length=2000, widget=forms.TextInput(attrs={'placeholder': 'Message', "class": "form-control"}))

    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'message']
