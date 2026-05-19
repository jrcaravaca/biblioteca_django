from django.db import models
from .book_model import Book
from django.contrib.auth.models import User


class Loan(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loans")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"