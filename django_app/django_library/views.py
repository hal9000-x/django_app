from django.shortcuts import render

from author.models import Author
from book.models import Book


def home_page(request):

    template_name = 'home_page.html'
    total_author = Author.objects.all().count()
    total_book = Book.objects.all().count()
    context = {"total_author": total_author, "total_book": total_book}
    return render(request, template_name, context)
