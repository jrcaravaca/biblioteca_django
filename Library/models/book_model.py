from django.db import models
from .author_model import Author
from ..constants import GENRE_CHOICES, LANGS_CHOICES


class Book(models.Model): 
    title = models.CharField('Titulo',max_length=100, unique=True, blank=False, null=False)
    language = models.CharField('Idioma',max_length=2, choices=LANGS_CHOICES, default='ES', blank=False, null=False)
    genre = models.CharField('Genero',max_length=10, choices=GENRE_CHOICES, default='OTHER', blank=False, null=False)
    synopsis = models.TextField('Sinopsis', blank=False, null=False)
    author = models.ManyToManyField(Author, related_name='books', blank=False)
    editorial = models.CharField('Editorial',max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True) 
    cantidad = models.PositiveIntegerField('Cantidad Disponible', default=1)
    frontpage = models.ImageField('Portada', upload_to='books/covers/', blank=True, null=True)

    @property
    def out_of_stock(self):
        return self.cantidad <= 0
    
    def __str__(self):
        status = ["SIN STOCK"] if self.out_of_stock else f"{self.cantidad} uds"
        return f"{self.title} - {status}"