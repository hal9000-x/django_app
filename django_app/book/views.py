from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.admin.views.decorators import staff_member_required

from author.models import Author
from .models import Book
from .forms import BookModelForm


def book_list(request):
    qs = Book.objects.all()
    template_name = 'book/list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


def book_details(request, id):
    try:
        #obj = Author.objects.get(id=id)
        obj = get_object_or_404(Book, id=id)
    except Book.DoesNotExists:
        raise Http404
    template_name = 'book/details.html'
    context = {"book": obj}
    return render(request, template_name, context)


@staff_member_required
def book_create(request):
    form = BookModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        
        print(form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        form = BookModelForm()
    template_name = 'author/form.html'
    context = {"form": form, "title": "new author form"}
    return render(request, template_name, context)


@staff_member_required
def book_update(request, id):
    obj = get_object_or_404(Author, id=id)
    form = AuthorModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'author/form.html'
    context = {"form": form, "title": f"Update Author: {obj.name}"}
    return render(request, template_name, context)


@staff_member_required
def book_delete(request, id):
    obj = get_object_or_404(Author, id=id)
    template_name = 'author/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/authors")
    context = {"object": obj, "form": None}
    return render(request, template_name, context)
