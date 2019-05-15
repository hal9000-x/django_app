from django import forms

from .models import Book


class AuthorForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'preview']
