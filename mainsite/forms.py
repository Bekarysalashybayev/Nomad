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


class IssueCreate(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['insurance', 'fio', 'iin', 'bday', 'doc1', 'doc3', 'phone', 'email', 'total']