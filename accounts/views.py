from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register_view(request):
    """Vista para el registro de nuevos usuarios."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente tras el registro
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def home_view(request):
    """
    Vista principal: determina el rol del usuario actual
    (Administrador, Gestor, Usuario o Visitante) para condicionar la interfaz.
    """
    user = request.user
    user_role = 'Visitante'

    if user.is_authenticated:
        if user.is_superuser or user.groups.filter(name='Administrador').exists():
            user_role = 'Administrador'
        elif user.groups.filter(name='Gestor').exists():
            user_role = 'Gestor'
        else:
            user_role = 'Usuario'

    context = {
        'user_role': user_role
    }
    return render(request, 'home.html', context)