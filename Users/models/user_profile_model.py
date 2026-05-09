from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    profile_picture = models.ImageField('Imagen de perfil', upload_to='profile_pictures/', blank=True, null=True)
    register_date = models.DateTimeField('Fecha de registro', auto_now_add=True)
    email = models.EmailField('Correo electrónico', max_length=254)
    dni = models.CharField('DNI', max_length=20)
    
    
    class Meta: 
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self): 
        return self.user.username
    
    