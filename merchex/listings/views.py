from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from listings.models import Film
from django.contrib.auth.models import User
"""from listings.models import UserFilm"""
from datetime import datetime
from listings.forms import FilmForm, ContactUsForm
from django.core.mail import send_mail

""" AJOUT DES FILMS """

def accueil(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect('accueil') 
    else:
        form = FilmForm()

    films = Film.objects.all()
    today = datetime.today().strftime('%d/%m/%Y')
    
    contexte = {
        'films': films,
        'date_du_jour': today,
        'form': form
    }
    return render(request, 
                  'listings/accueil.html', 
                  contexte)
# render => crée un objet HttpResponse avec le HTML
# dictionnaire contextuel pour créer des gabarits     

""" FILMOTHEQUE + GESTION FILMS """

def filmotheque(request):
    films = Film.objects.all()
    return render(request, 
                  'listings/filmotheque.html', 
                  {'films': films})

def changer_statut(request, film_id):
    film = Film.objects.get(id=film_id)
    if film.statut == 'AVOIR':
        film.statut = 'VU'
    else:
        film.statut = 'AVOIR'
    film.save()
    return redirect('filmotheque')

def modifier_film(request, film_id):
    film = Film.objects.get(id=film_id)
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film) # préremplir le form avec le groupe existant
        if form.is_valid():
            form.save() # màj dans la BDD
            return redirect('filmotheque')
    else:
        form = FilmForm(instance=film)

    return render(request, 
                  'listings/modifier_film.html', 
                  {'form': form})

def supprimer_film(request, film_id):
    film = Film.objects.get(id=film_id)
    if request.method == 'POST':
        film.delete()
        return redirect('filmotheque')
    return render(request, 
                  'listings/supprimer_film.html', 
                  {'film': film})

""" VUE DETAILLEE DES FILMS """

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request,
                  'listings/film_detail.html',
                  {'film': film})

""" PAGE DE CONTACT """

def contact(request):
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-envoyé')
# si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
# ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request, 
                  'listings/contact.html',
                  {'form': form})

def email_envoye(request):
    return render(request, 'listings/email_envoye.html')
