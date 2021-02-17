# Importing Django RESTFramework's generics class of views
from rest_framework import generics
# Import the models from our books app
from books.models import Book
# Importing serializers from our api app
# A serializer translates data into a format that is easy to consume over the internet. Typically displayed in JSON at an API endpoint.
from .serializers import BookSerializer

# Creatign a class that uses ListAPIView to create a read-only endpoint for all book instances.
class BookAPIView(generics.ListAPIView):
    # queryset is all available books
    queryset = Book.objects.all()
    serializer_class = BookSerializer