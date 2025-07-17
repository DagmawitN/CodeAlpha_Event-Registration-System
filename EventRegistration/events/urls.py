from django.urls import path
from .views import (EventListView,EventDetailView,RegisterEventView,MyRegistrationView,CancelRegistrationView)

urlpatterns = [
    path('events/',EventListView.as_view(),name='event-list'),
    path('events/<int:pk>/',EventDetailView.as_view(),name='event-detail'),
    path('register/',RegisterEventView.as_view(),name='register-event'),
    path('myregistration/',MyRegistrationView.as_view(),name='my-registration'),
    path('cancelregistration/<int:pk>/',CancelRegistrationView.as_view(),name='cancel-registration'),
]