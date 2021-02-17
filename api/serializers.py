# Importing REST Framework's serializers class
from rest_framework import serializers
# Importing Book model from our books app.
from books.models import Book

# We extend Django REST Framework's ModelSerializer into a BookSerializer class that specifies our database model Book and the database fields we with to expose.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "subtitle",
            "author",
            "isbn",
        )

