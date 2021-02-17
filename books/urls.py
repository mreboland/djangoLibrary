from django.urls import path
# Import our views file so we can use it on page
from .views import BookListView

urlpatterns = [
    # Empty string indicates our view is what is shown on home. Gave it a named URL of 'home' to reference.
    # The full 
    path("", BookListView.as_view(), name="home"),
]