from django.urls import path
from .views import EventCreate, EventDeleteView, EventDetailView, EventListView, EventUpdateView

urlpatterns = [
    path('', EventListView.as_view(), name='eventlist'),
    path('create', EventCreate.as_view(), name='create'),
    path('update/<int:pk>', EventUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', EventDeleteView.as_view(), name='delete'),
    path('/<int:pk>', EventDetailView.as_view(), name='view'),

]