from django.db import models

class Author(models.Model): 
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    nationality = models.CharField('Nacionalidad', max_length=100)
    biography = models.TextField('Biografía', blank=True, null=True)
    birth_date = models.DateField('Fecha de nacimiento',blank=True, null=True)
    death_date = models.DateField('Fecha de fallecimiento',blank=True, null=True)
    

    def __str__(self):
        return f"{self.name} {self.last_name}"