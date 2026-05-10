from .models.book_model import Book, Review
from django import forms

# class BookCreateForm(ModelForm): 
#     class Meta: 
#         model = Post
#         fields = [
#             'image', 
#             'caption'
#         ]


class ReviewCreateForm(forms.ModelForm): 
    class Meta: 
        model = Review
        fields = [
            'review',
            'puntuacion'
        ]

