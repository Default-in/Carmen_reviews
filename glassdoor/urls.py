from django.urls import path
from .views import table, multiplewords, companyInfo, reviewsInfo
from .models import GlassdoorReview

qs = GlassdoorReview.objects.all()

urlpatterns = [
    path('glassdoor/table', table),
    path('glassdoor/multiplewords', multiplewords),
    path('glassdoor/companiesinfo', companyInfo),
    path('glassdoor/company/<int:pk>', reviewsInfo),
]
