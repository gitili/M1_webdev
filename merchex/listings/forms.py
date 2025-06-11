# listings/forms.py

from django import forms
from listings.models import Film

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class FilmForm(forms.ModelForm):
   class Meta:
     model = Film
     fields = '__all__'
