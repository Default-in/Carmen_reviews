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


def reviewsInfo(request, pk):
    qs = IndeedReview.objects.get(pk=pk)
    search_word = request.GET.get('word')
    print(search_word)

    word = "life"
    # company_info_list = []
    # company_info = {
    #     'company_name': qs.companyName,
    #     'total_reviews': qs.totalReviews,
    #     'overall_rating': qs.overallRatings,
    # }
    list_to_show = []
    date_list = list(qs.reviewDate.splitlines())
    headings = list(qs.reviewHeadings.splitlines())
    descriptions = list(qs.reviewDescriptions.splitlines())
    # print(date_list)
    # print(pros)
    # print(cons)
    # print(headings)
    # print(descriptions)

    reviews_headings = list(qs.reviewHeadings.replace('"', '').split())
    reviews_descriptions = list(qs.reviewDescriptions.replace('"', '').split())

    conditions = [
        word in reviews_headings,
        word in reviews_descriptions,
    ]

    total_reviews = len(date_list)
    for i in range(total_reviews):
        if search_word in headings[i] or word in descriptions[i]:
            # print(date_list[i])
            # print(headings[i])
            # print(descriptions[i])
            # print(pros[i])
            # print(cons[i])
            # print("=======================\n")
            result_list = {
                "review_date": date_list[i],
                "review_heading": headings[i],
                "review_descriptions": descriptions[i],
            }

            list_to_show.append(result_list)
            # pass
        else:
            # print(f"No - {i}")
            pass

    context = {
        'pk': pk,
        'queryset': list_to_show,
    }

    return render(request, 'indeedreviewinfo.html', context)
