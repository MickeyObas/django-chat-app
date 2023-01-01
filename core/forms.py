from django import forms
from .models import Room, Message

class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['creator', 'participants']