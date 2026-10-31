from django.db import models
from django.contrib.auth.models import User

# Modelo que extiende el usuario estándar de Django mediante relación 1 a 1
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.png', upload_to='users/', null=True, blank=True, verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username