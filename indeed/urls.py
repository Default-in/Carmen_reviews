from django.urls import path
from .views import table, reviewsInfo


urlpatterns = [
    path('indeed/table', table),
    path('indeed/company/<int:pk>', reviewsInfo),
]
