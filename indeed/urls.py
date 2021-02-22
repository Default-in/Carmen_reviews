from django.urls import path
from .views import table


urlpatterns = [
    path('indeed/table', table),
]
