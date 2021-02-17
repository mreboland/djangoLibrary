# Importing Django RESTFramework's generics class of views
from rest_framework import generics
# Import the models from our books app
from books.models import Book
# Importing serializers from our api app
from .serializers import BookSerializer

# Creatign a class that uses ListAPIView to create a read-only endpoint for all book instances.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer