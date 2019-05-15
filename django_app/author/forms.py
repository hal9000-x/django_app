from django import forms

from .models import Author


class AuthorForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'phone']
