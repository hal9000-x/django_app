from django.shortcuts import render

# Create your views here.

from book.models import Book

from .models import Search


def search(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        Search.objects.create(user=user, query=query)
        book_list = Book.objects.search(query=query)
        context['book_list'] = book_list
    return render(request, 'search/search.html', context)
