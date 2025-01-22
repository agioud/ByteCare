from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_probability, name='home'),  # Page d'accueil pour Predictor
    path('predict/', views.calculate_probability, name='predict'),  # Formulaire de prédiction
]

