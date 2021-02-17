# Importing ListView which is a page respresinting a list of objects
from django.views.generic import ListView
# Importing our Book model
from .models import Book

# Created a class that specified the model to use and the template
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    
    