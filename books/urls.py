from django.urls import path
# Import our views file so we can use it on page
from .views import BookListView

urlpatterns = [
    # Empty string indicates our view is what is shown on home. Gave it a named URL of 'home' to reference.
    # The full pathing when a user goes to the homepage of our site is they will first hit the config/urls.py file, then be redirected to books/urls.py which specifies using the BookListView. In this file, the Book model is used along with ListView to list out all books.
    path("", BookListView.as_view(), name="home"),
]