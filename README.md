# Merchex - Gestion de films

Merchex est une application web Django pour gérer ta collection de films. 
C'est un projet réalisé dans le cadre de mon cours de web programmation de M1, à partir d'OpenClassrooms (https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django).

## Fonctionnalités

- Ajouter, modifier et supprimer des films
- Afficher les détails de chaque film (titre, résumé, durée, année, etc)
- Gérer le statut de chaque film : "Vu" ou "À voir"

## Installation

```bash
git clone https://github.com/gitili/M1_webdev.git
cd django-web-app
python -m venv env
pip install -r requirements.txt
```
## Lancement

```bash
cd django-web-app
env\Scripts\activate
cd merchex
python manage.py runserver
```
-> Rends-toi sur http://localhost:8000/accueil pour commencer à gérer tes films.
