from django import forms
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField(max_length=126)
    email=forms.EmailField(max_length=256)
    verify_email=forms.EmailField(max_length=256)
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean=super().clean()
        email=all_clean['email']
        verify_email=all_clean['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Emails do not match')
