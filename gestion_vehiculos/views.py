from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Automovil


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Te has registrado correctamente. Por favor, inicia sesión.")
            return redirect('login')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = UserRegistrationForm()
    return render(request, 'gestion_vehiculos/register.html', {'form': form})

@login_required
def home(request):
    user = request.user
    return render(request, 'gestion_vehiculos/home.html', {'user': user})

class CustomLoginView(LoginView):
    template_name = 'gestion_vehiculos/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, "Has iniciado sesión con éxito.")
        login(self.request, user)
        print(f"Usuario autenticado: {user}")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al iniciar sesión. Por favor, revisa tus credenciales.")
        return super().form_invalid(form)
    

def catalogo(request):
    automoviles = Automovil.objects.all()
    return render(request, 'gestion_vehiculos/catalogo.html', {'automoviles': automoviles})

def detalle_automovil(request, automovil_id):
    automovil = get_object_or_404(Automovil, id=automovil_id)
    return render(request, 'gestion_vehiculos/detalle_automovil.html', {'automovil': automovil})


def test_view(request):
    return render(request, 'gestion_vehiculos/test.html')