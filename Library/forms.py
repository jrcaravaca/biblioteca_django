from .models.book_model import Book, Review
from .models.author_model import Author
from django import forms
from dal import autocomplete

class BookCreateForm(forms.ModelForm): 
    class Meta: 
        model = Book
        fields = [
            'title', 
            'language', 
            'genre', 
            'synopsis', 
            'author',   
            'editorial', 
            'publication_date', 
            'isbn', 
            'cantidad', 
            'frontpage'
        ]
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'author': autocomplete.ModelSelect2Multiple(
                url='author-autocomplete',
                attrs={
                    'data-placeholder': 'Buscar autor...',
                    'data-minimum-input-length': 3,
                }
            )
        }





class ReviewCreateForm(forms.ModelForm): 
    class Meta: 
        model = Review
        fields = [
            'review',
            'puntuacion'
        ]


class AuthorCreateForm(forms.ModelForm): 
    class Meta: 
        model = Author
        fields= [
            'name',
            'last_name', 
            'nationality', 
            'biography', 
            'birth_date',
            'death_date'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'death_date': forms.DateInput(attrs={'type': 'date'}),
        }
