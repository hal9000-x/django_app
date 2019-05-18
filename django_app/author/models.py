from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class Author(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=120)
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def get_absolute_url(self):
        return f"/authors/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
