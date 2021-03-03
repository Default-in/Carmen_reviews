from django.urls import path
from .views import table, reviewsInfo, multiplewords, companyInfo, single_and_multiple_words, download_csv_single_word


urlpatterns = [
    # path('indeed/singleword', table),
    path('indeed/company/<int:pk>', reviewsInfo),
    path('indeed/download/<int:pk>', download_csv_single_word),
    # path('indeed/multiplewords', multiplewords),
    path('indeed/companiesinfo', companyInfo),
    path('indeed', single_and_multiple_words),
]
