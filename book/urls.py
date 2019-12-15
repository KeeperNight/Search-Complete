from django.urls import path
from .views import (
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    AuthorBookListView
)
from . import views

urlpatterns = [
    path('book_list/',views.home, name="books"),
    path('author/<str:username>', AuthorBookListView.as_view(), name="author-book"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('new/', BookCreateView.as_view(), name="book-create"),
]
