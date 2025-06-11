from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.contrib.auth.models import User

current_year = datetime.date.today().year

# ---------- FILM ---------- #
# Film = infos générales valables pour tous
class Film(models.Model): # .Model => classe de base des modèles
    STATUT_CHOICES = [
        ('VU', 'Vu'),
        ('AVOIR', 'À voir'),
    ]
    statut = models.CharField(
        max_length=6,
        choices=STATUT_CHOICES,
        default='AVOIR'
    )
    name = models.CharField(max_length=100)
    # attribut de classe auquel nous attribuons un champ (attribut)
    date_sortie = models.IntegerField(
        null=True, 
        blank=True,
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(current_year + 1)
            ]
    )
    duree = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=20)
    synopsis = models.URLField(null=True, blank=True)
    
    class Meta:
        unique_together = ('name', 'date_sortie')  # pour éviter les doublons exacts

    # pour afficher + de détails sur l'objet dans l'admin ou la console
    def __str__(self): 
        return f'{self.name} ({self.date_sortie})'
