from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import UserPassesTestMixin
from django import forms

from ..models.book_model import Book
from ..models.author_model import Author
from ..models.loan_model import Loan
from ..forms import ReviewCreateForm, BookCreateForm




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
        active_loans = Loan.objects.filter(user=self.request.user, returned=False)
        context['form'] = self.get_form()
        context['loaned'] = active_loans.filter(book=self.object).exists()
        context['active_loans_count'] = active_loans.count()

        return context
    
    def get_success_url(self):
        return reverse('book-detail', args=[self.get_object().pk])
    

@method_decorator(login_required, name='dispatch')
class BookCreateView(UserPassesTestMixin, CreateView): 
    template_name = "books/book_create.html"
    model = Book
    success_url = reverse_lazy('home')
    form_class = BookCreateForm

    def form_valid(self, form): 
        form.instance.user = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Libro creado correctamente')
        return super(BookCreateView, self).form_valid(form)
    
    def test_func(self): 
        return self.request.user.groups.filter(name="staff").exists()

    def handle_no_permission(self):
        return redirect('access-denied')
    

@method_decorator(login_required, name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 10

    
@method_decorator(login_required, name='dispatch')
class BookDeleteView(UserPassesTestMixin,DeleteView): 
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy('home')
    
    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Libro eliminado correctamente")
        return super().post(request, *args, **kwargs)
    
    def test_func(self): 
        return self.request.user.groups.filter(name="staff").exists()

    def handle_no_permission(self):
        return redirect('access-denied')

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UserPassesTestMixin, UpdateView, FormView): 
    model = Book
    template_name = "books/book_update.html"
    context_object_name = "book"
    form_class = BookCreateForm

    def form_valid(self, form): 
        messages.add_message(self.request, messages.SUCCESS, "Libro editado correctamente")
        return super(BookUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('book-detail', args=[self.object.pk])
    
    def test_func(self): 
        return self.request.user.groups.filter(name="staff").exists()

    def handle_no_permission(self):
        return redirect('access-denied')
    

