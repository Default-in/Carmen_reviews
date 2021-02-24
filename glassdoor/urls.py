from django.urls import path
from .views import table, multiplewords, companyInfo, reviewsInfo, test, testtable, singlewordboth, Home, single_and_multiple_words, both_platforms
from .models import GlassdoorReview

qs = GlassdoorReview.objects.all()

urlpatterns = [
    # path('glassdoor/singleword', table),
    # path('glassdoor/multiplewords', multiplewords),
    path('glassdoor/companiesinfo', companyInfo),
    path('glassdoor/company/<int:pk>', reviewsInfo),
    path('', single_and_multiple_words),
    path('test', test),
    path('glassdoor/', testtable),
    # path('both', singlewordboth),
    path('both', both_platforms),
]

