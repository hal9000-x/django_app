from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.admin.views.decorators import staff_member_required

from .models import Author
from .forms import AuthorModelForm

def author_list(request):
    qs = Author.objects.all()
    template_name = 'author/list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


def author_details(request, id):
    try:
        #obj = Author.objects.get(id=id)
        obj = get_object_or_404(Author, id=id)
    except Author.DoesNotExists:
        raise Http404
    template_name = 'author/details.html'
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def author_create(request):
    form = AuthorModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        #obj = form.save(commit=False)
        #obj.name = form.cleaned_data.get("name") + "-test!!!"
        #obj.save()
        #obj = Author.objects.create(**form.cleaned_data)
        form = AuthorModelForm()
    template_name = 'author/form.html'
    context = {"form": form, "title":"Create New Author:"}
    return render(request, template_name, context)


@staff_member_required
def author_update(request, id):
    obj = get_object_or_404(Author, id=id)
    form = AuthorModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'author/form.html'
    context = {"form": form, "title": f"Update Author: {obj.name}"}
    return render(request, template_name, context)


@staff_member_required
def author_delete(request, id):
    obj = get_object_or_404(Author, id=id)
    template_name = 'author/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/authors")
    context = {"object": obj, "form": None}
    return render(request, template_name, context)
