from django import forms

from .models import *


class FormCreate(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'description']


class NewsCreate(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'description', 'img']