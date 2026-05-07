from django.contrib import admin
from .models.loan_model import Loan
from .models.book_model import Book
from .models.author_model import Author

admin.site.register(Loan)
admin.site.register(Book)
admin.site.register(Author)

# Register your models here.
