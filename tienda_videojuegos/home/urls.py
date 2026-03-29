from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # Ruta principal, lleva al index
    path('contacto/', views.contacto, name='contacto'), # Ruta de contacto, lleva al contacto
]