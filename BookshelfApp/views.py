from rest_framework.views import APIView
from .models import Book
from rest_framework.response import Response
from .serializer import BookSerializer
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login") 
    template_name = "registration/signup.html"

class BookListView(ListView):
    model = Book
    template_name = "BookshelfApp/index.html"

    def get_queryset(self):
        books = Book.objects.all() 
        user_books = books.filter(user=self.request.user)
        return user_books

    def get(self, request):
        return super().get(request)

class book_list(APIView):
    def get(self, request):
        books = Book.objects.all() 
        user_books = books.filter(user=self.request.user)
        serializer = BookSerializer(user_books, many=True)
        return Response(serializer.data)


class add_book(CreateView):
    model = Book
    fields = ["title", "author", "number_of_pages", "status"]

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class book_detail(ListView):
    model = Book
    template_name = "BookshelfApp/book_detail.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["Book"] = Book.objects.get(id=self.kwargs["pk"])
        return context

class update_status(APIView):
    def post(self, request):
        book = Book.objects.get(id=request.POST.get("id"))
        if book.status:
            book.status = False
        else:
            book.status = True
        book.save()
        return Response(status=200, data={
            "book": book.id

        })


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("home")


