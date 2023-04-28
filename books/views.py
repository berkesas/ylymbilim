import os
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(status=1)
    serializer_class = BookSerializer


def download_epub(request, pk):
    book = Book.objects.get(id=pk)
    file_path = book.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/epub+zip")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404