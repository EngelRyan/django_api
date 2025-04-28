from django.urls import path
from .views import get_persons

urlpatterns = [
    path('persons/', get_persons, name='get_persons'),
]