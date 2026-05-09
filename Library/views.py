from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models.book_model import Book
from .models.author_model import Author


# Create your views here.
@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

   
