from .models import *


qs = GlassdoorReview.objects.all()

# data = GlassdoorReview.objects.get(pk=7)
# print(data.companyUrl)

companies_list = []
for item in qs:
    company = item.companyName
    companies_list.append(company)

print(companies_list)
