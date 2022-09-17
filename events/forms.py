from django import forms
from .models import Event 


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'category',
         'start_date', 'end_date', 
         'start_time', 'end_time', 
         'venue', 'ticket_price',
         'description')