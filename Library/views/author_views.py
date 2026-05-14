from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from dal import autocomplete
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin


from ..models.book_model import Book
from ..models.author_model import Author
from ..forms import AuthorCreateForm

@method_decorator(login_required, name='dispatch')
class AuthorCreateView(UserPassesTestMixin, CreateView): 
    template_name = "authors/author_create.html"
    model = Author
    success_url = reverse_lazy('home')
    form_class = AuthorCreateForm

    def form_valid(self, form): 
        
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Autor creado correctamente')
        return super(AuthorCreateView, self).form_valid(form)
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url: 
            return next_url

        return super().get_success_url()
     
    def test_func(self): 
        return self.request.user.groups.filter(name="staff").exists()

    def handle_no_permission(self):
        return redirect('access-denied')


@method_decorator(login_required, name='dispatch')
class AuthorDetailView(DetailView): 
    model = Author
    template_name = "authors/author_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.object.pk)
 
        return context
    

@method_decorator(login_required, name='dispatch')
class AuthorListView(ListView):
    model = Author
    template_name = "authors/author_list.html"
    context_object_name = "authors"
    paginate_by = 10

@method_decorator(login_required, name='dispatch')
class AuthorDeleteView(UserPassesTestMixin, DeleteView): 
    model = Author
    template_name = "authors/author_delete.html"
    success_url = reverse_lazy('home')
    
    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Autor eliminado correctamente")
        return super().post(request, *args, **kwargs)
    
    def test_func(self): 
        return self.request.user.groups.filter(name="staff").exists()

    def handle_no_permission(self):
        return redirect('access-denied')
    

@method_decorator(login_required, name='dispatch')
class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        qs = Author.objects.all()
        if self.q:
            qs = qs.filter(
                Q(name__icontains=self.q)  |
                Q(last_name__icontains=self.q)
            )
        return qs
    

