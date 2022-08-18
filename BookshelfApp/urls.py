from django.urls import path
from .views import BookDelete, BookListView, SignUpView, add_book, book_detail, book_list, update_status

urlpatterns = [
    path("", SignUpView.as_view(), name="signup"),
    path('book/list/', book_list.as_view(), name = "book_list"),
    path('add/book/', add_book.as_view(), name="add-book"),
    path('book/<int:pk>/', book_detail.as_view(), name="book"),
    path("home/", BookListView.as_view(), name="home"),
    path("book/<int:pk>/delete/", BookDelete.as_view(), name="book-delete"),
    path("update/book/", update_status.as_view(), name="book-update")
    
]