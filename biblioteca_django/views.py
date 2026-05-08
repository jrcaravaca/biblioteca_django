from django.views.generic import TemplateView
from Library.models.book_model import Book


class HomeView(TemplateView): 
    template_name = 'general/home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        books = Book.objects.all()
        context['books'] = books
        
        return context