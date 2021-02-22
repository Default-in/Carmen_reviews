from django.shortcuts import render
from .models import IndeedReview

# Create your views here.
def table(request):
    qs = IndeedReview.objects.all()
    word = request.GET.get("word")
    print(word)

    list_to_show = []
    for company in qs:
        total_reviews = len(list(company.reviewDate.splitlines()))
        if total_reviews != 0:
            id = company.id
            reviews_headings = company.reviewHeadings.replace('"', '').split()
            reviews_descriptions = company.reviewDescriptions.replace('"', '').split()

            total_count = 0
            total_heading = 0
            total_desc = 0
            company_url = company.companyUrl
            for rev in reviews_headings:
                if str(word) in rev.lower():
                    total_heading += 1
                    total_count += 1

            for rev in reviews_descriptions:
                if str(word) in rev.lower():
                    total_desc += 1
                    total_count += 1

            result_list = {
                'id': id,
                'company_name': company.companyName,
                'wc_in_heading': total_heading,
                'wc_in_descriptions': total_desc,
                'total_count': total_count,
                'total_Reviews': total_reviews,
                'company_url': company_url,
            }
            list_to_show.append(result_list)
        else:
            pass

    list_to_show = sorted(list_to_show, key=lambda j: j['total_count'], reverse=True)
    print(len(list_to_show))

    context = {
        'word': word,
        'queryset': list_to_show,
    }

    return render(request, 'indeedtable.html', context)
