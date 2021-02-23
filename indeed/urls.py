from django.urls import path
from .views import table, reviewsInfo, multiplewords, companyInfo


urlpatterns = [
    path('indeed/singleword', table),
    path('indeed/company/<int:pk>', reviewsInfo),
    path('indeed/multiplewords', multiplewords),
    path('indeed/companiesinfo', companyInfo),
]
