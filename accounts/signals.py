from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import Profile

# Crea el perfil y asigna el grupo básico cuando se registra un nuevo usuario
@receiver(post_save, sender=User)
def create_user_profile_and_role(sender, instance, created, **kwargs):
    if created:
        # Crear perfil
        Profile.objects.create(user=instance)
        
        # Obtener o crear grupo por defecto para nuevos registros
        user_group, _ = Group.objects.get_or_create(name='Usuario')
        instance.groups.add(user_group)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()