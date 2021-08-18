from django import forms
from django.forms import HiddenInput


class ContactForm(forms.Form):
    title = forms.CharField(max_length=200)
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    to = forms.EmailField(required=False, initial='owoborodeseye@gmail.com')
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['to'].widget = HiddenInput()
