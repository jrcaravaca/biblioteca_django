from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models.book_model import Book
from .models.author_model import Author
from .forms import ReviewCreateForm



# Create your views here.
@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView, FormView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    form_class = ReviewCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form): 
        form.instance.user = self.request.user
        form.instance.book = self.get_object()
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Reseña añadida correctamente')
        return super(BookDetailView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('book-detail', args=[self.get_object().pk])