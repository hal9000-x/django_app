from django.conf import settings
from django.db import models
from author.models import Author

from django.db.models import Q

User = settings.AUTH_USER_MODEL


class BookQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
            Q(name__icontains=query) |
            Q(preview__icontains=query) |
            Q(author__name__icontains=query)
        )
        return self.filter(lookup)


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def search(self, query=None):
        print("hello")
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Book(models.Model):

    name = models.CharField(max_length=120)
    author = models.ForeignKey(Author, default=1, null=True, on_delete=models.SET_NULL)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    preview = models.TextField(null=True, blank=True)

    # ImageField require pillow. run 'pipenv install pillow'
    cover_image = models.ImageField(upload_to='image/', blank=True, null=True)

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    objects = BookManager()
    
    class Meta:
        ordering = ['-created_at', '-updated_at']

    def get_absolute_url(self):
        return f"/books/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
