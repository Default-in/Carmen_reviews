from .models import *


qs = IndeedReview.objects.all()


companies_list = []
for item in qs:
    company = item.companyName
    companies_list.append(company)

print(companies_list)
