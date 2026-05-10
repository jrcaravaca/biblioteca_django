from .models.book_model import Book, Review
from django import forms

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
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }



class ReviewCreateForm(forms.ModelForm): 
    class Meta: 
        model = Review
        fields = [
            'review',
            'puntuacion'
        ]

