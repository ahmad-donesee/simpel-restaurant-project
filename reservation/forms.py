from django import forms 
from . models import Reserve

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reserve
        fields="__all__"
        # fields=("name","email","phone","number","date","time")
