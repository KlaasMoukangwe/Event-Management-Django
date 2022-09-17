from dataclasses import fields
from multiprocessing import Event
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Event

# Create your views here.
class EventListView(ListView):
    model = Event
    template_name = 'eventlist.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('eventlist')
    template_name = 'event_confirm_delete.html'

class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'category', 'start_date', 'end_date', 'start_time', 'end_time','ticket_price', 
                'available_tickets', 'venue', 'description',]
    success_url = reverse_lazy('eventlist')
    template_name = 'update_form.html'


class EventCreate(CreateView):
    template_name = 'create_event.html'
    model = Event
    fields = ['title', 'category', 'start_date', 'end_date', 'start_time', 'end_time','ticket_price', 'available_tickets', 'venue', 'description',]
    success_url = reverse_lazy('eventlist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)

