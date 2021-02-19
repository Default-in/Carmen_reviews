from django.urls import path
from .views import table, multiplewords, companyInfo

urlpatterns = [
    path('table', table),
    path('multiplewords', multiplewords),
    path('companiesinfo', companyInfo),
]
