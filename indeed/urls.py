from django.urls import path
from .views import table, reviewsInfo, multiplewords


urlpatterns = [
    path('indeed/singleword', table),
    path('indeed/company/<int:pk>', reviewsInfo),
    path('indeed/multiplewords', multiplewords),
]
