from django.contrib import admin

# Register your models here.

from listings.models import Film

class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_sortie')

admin.site.register(Film, FilmAdmin)
