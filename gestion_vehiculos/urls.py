from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('test/', views.test_view, name='test'),
    path('automovil/<int:automovil_id>/', views.detalle_automovil, name='detalle_automovil'),
]
    