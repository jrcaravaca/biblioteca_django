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
                }),
            'frontpage': forms.FileInput(attrs={'class': 'block w-full text-sm text-black file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 '
                                                     'file:text-sm file:font-semibold file:bg-pink-500 file:text-white hover:file:bg-pink-600'
                })
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
            'death_date',
            'photo'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'death_date': forms.DateInput(attrs={'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'block w-full text-sm text-black file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 '
                                                     'file:text-sm file:font-semibold file:bg-pink-500 file:text-white hover:file:bg-pink-600'})
        }
