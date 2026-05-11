from django.db import models
from django.db.models import Avg
from .author_model import Author
from ..constants import GENRE_CHOICES, LANGS_CHOICES


class Book(models.Model): 
    title = models.CharField('Titulo',max_length=100, unique=True, blank=False, null=False)
    language = models.CharField('Idioma',max_length=2, choices=LANGS_CHOICES, default='ES', blank=False, null=False)
    genre = models.CharField('Genero', choices=GENRE_CHOICES, default='OTHER', blank=False, null=False)
    synopsis = models.TextField('Sinopsis', blank=False, null=False)
    author = models.ManyToManyField('Author', verbose_name='Autor', related_name='books', blank=False)
    editorial = models.CharField('Editorial',max_length=100)
    publication_date = models.DateField('Fecha de publicación')
    isbn = models.CharField('ISBN',max_length=13, unique=True) 
    cantidad = models.PositiveIntegerField('Cantidad Disponible', default=1)
    frontpage = models.ImageField('Portada', upload_to='books/covers/', blank=True, null=True)

    @property
    def out_of_stock(self):
        return self.cantidad <= 0
    
    @property
    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('puntuacion'))['avg'] or "Aún no hay reseñas"  
    
    def __str__(self):
        status = ["SIN STOCK"] if self.out_of_stock else f"{self.cantidad} uds"
        return f"{self.title} - {status}"
    

class Review(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='usuario')
    review = models.TextField('Reseña', max_length=1500, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha de creación del comentario')
    puntuacion = models.PositiveIntegerField('Puntuación', blank=False, null=False, choices=((i,i) for i in range (1,11)))

    class Meta: 
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"