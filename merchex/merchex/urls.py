"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # création modèle d'URL et liaison à notre vue
    path('accueil/', views.accueil, name='accueil'),
    path('filmotheque/', views.filmotheque, name='filmotheque'),
    path('changer-statut/<int:film_id>/', views.changer_statut, name='changer_statut'),
    path('modifier-film/<int:film_id>/', views.modifier_film, name='modifier_film'),
    path('supprimer-film/<int:film_id>/', views.supprimer_film, name='supprimer_film'),
    path('filmotheque/<int:film_id>/', views.film_detail, name='film_detail'),
    path('contact/', views.contact, name='contact'),
    path('email-envoye/', views.email_envoye, name='email-envoyé')
]
