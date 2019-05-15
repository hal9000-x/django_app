"""django_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import (
    home_page,
)

from author.views import (
    author_list,
    author_create,
    author_details,
    author_update,
    author_delete,
)

from book.views import (
    book_list,
    book_create,
    book_details,
    book_update,
    book_delete,
)

urlpatterns = [
    path('', home_page),

    path('authors/new', author_create),
    path('authors/', author_list),
    path('authors/<int:id>/', author_details),
    path('authors/<int:id>/edit', author_update),
    path('authors/<int:id>/delete', author_delete),

    path('books/new', book_create),
    path('books/', book_list),
    path('books/<int:id>/', book_details),
    path('books/<int:id>/edit', book_update),
    path('books/<int:id>/delete', book_delete),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
