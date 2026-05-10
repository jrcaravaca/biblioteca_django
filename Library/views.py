from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone

from .models.book_model import Book
from .models.author_model import Author
from .models.loan_model import Loan
from .forms import ReviewCreateForm



# Create your views here.
@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView, FormView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    form_class = ReviewCreateForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 

        if request.POST.get('action') == 'loan': 
            return self.handle_loan()
        
        return super().post(request, *args, **kwargs)


    def handle_loan(self): 
        book = self.get_object()
        if self.request.POST.get('action') == "loan": 
            if Loan.objects.filter(user=self.request.user, book=book, returned=False).exists():
                Loan.objects.filter(user=self.request.user, book=book, returned=False).update(returned=True, return_date=timezone.now())
                book.cantidad += 1
                book.save()
                messages.add_message(self.request, messages.SUCCESS, 'Libro devuelto correctamente')
                return redirect(self.get_success_url())
            else: 
                if book.cantidad <= 0: 
                    messages.add_message(self.request, messages.ERROR, 'No hay libros disponibles')
                    return redirect(self.get_success_url()) 
                
                Loan.objects.create(user=self.request.user, book=book, loan_date=timezone.now())
                book.cantidad -=1
                book.save()
                messages.add_message(self.request, messages.SUCCESS, 'Libro prestado correctamente')
                return redirect(self.get_success_url())
            
    
    def form_valid(self, form): 
        
        form.instance.user = self.request.user
        form.instance.book = self.get_object()
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Reseña añadida correctamente')
        return super(BookDetailView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        if not hasattr(self, 'object'):
            self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['loaned'] = Loan.objects.filter(user=self.request.user, book=self.object, returned=False).exists()

        return context
    
    def get_success_url(self):
        return reverse('book-detail', args=[self.get_object().pk])