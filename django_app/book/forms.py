from django import forms

from .models import Book


class BookForm(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    preview = forms.CharField()


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'published_at', 'cover_image', 'preview']
