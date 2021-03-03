from django.urls import path
from .views import table, multiplewords, companyInfo, reviewsInfo, \
    test, testtable, singlewordboth, Home, single_and_multiple_words, both_platforms, download_csv_single_word
from .models import GlassdoorReview

qs = GlassdoorReview.objects.all()

urlpatterns = [
    # path('glassdoor/singleword', table),
    # path('glassdoor/multiplewords', multiplewords),
    path('glassdoor/companiesinfo', companyInfo),
    path('company/<int:pk>', reviewsInfo),
    path('glassdoor/download/<int:pk>', download_csv_single_word),
    path('', single_and_multiple_words),
    path('test', test),
    path('glassdoor/', testtable),
    # path('both', singlewordboth),
    path('both', both_platforms),
]

