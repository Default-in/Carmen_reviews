from .models import GlassdoorReview
from django.shortcuts import render
from indeed.models import *


def table(request):
    qs = GlassdoorReview.objects.all()
    total = len(qs)
    word = request.GET.get('word')
    print(word)

    list_to_show = []
    for item in qs:
        # company = GlassdoorReview.objects.get(id=(i+1))
        company = item
        total_reviews = len(list(company.reviewDate.splitlines()))
        if total_reviews != 0:
            id = item.id
            reviews_headings = company.reviewHeadings.replace('"', '').split()
            reviews_descriptions = company.reviewDescriptions.replace('"', '').split()
            reviews_pros = company.reviewPros.replace('"', '').split()
            reviews_cons = company.reviewCons.replace('"', '').split()

            total_count = 0
            total_heading = 0
            total_desc = 0
            total_pros = 0
            total_cons = 0
            company_url = item.companyUrl
            for rev_h in reviews_headings:
                if str(word) in rev_h.lower():
                    total_heading += 1
                    total_count += 1

            for rev_d in reviews_descriptions:
                if str(word) in rev_d.lower():
                    total_desc += 1
                    total_count += 1

            for rev_p in reviews_pros:
                if str(word) in rev_p.lower():
                    total_pros += 1
                    total_count += 1

            for rev_c in reviews_cons:
                if str(word) in rev_c.lower():
                    total_cons += 1
                    total_count += 1

            result_list = {
                'id': id,
                'company_name': company.companyName,
                'wc_in_heading': total_heading,
                'wc_in_descriptions': total_desc,
                'wc_in_pros': total_pros,
                'wc_in_cons': total_cons,
                'total_count': total_count,
                'total_Reviews': total_reviews,
                'company_url': company_url,
            }
            list_to_show.append(result_list)
        else:
            pass

    list_to_show = sorted(list_to_show, key=lambda j: j['total_count'], reverse=True)
    print(len(list_to_show))
    # for item in list_to_show:
    #     print(item)

    context = {
        'word': word,
        'queryset': list_to_show,
    }

    return render(request, 'search.html', context)


def companyInfo(request):
    qs = GlassdoorReview.objects.all()

    main_list = []
    for item in qs:
        company_name = item.companyName
        overall_rating = item.overallRating
        total_reviews = item.totalReviews
        review = ''
        for char in total_reviews:
            if char != 'k':
                review += char
            else:
                review = float(review) * 1000

        recommend_to_friend = item.recommendToFriend
        approve_of_ceo = item.approveOfCEO
        jobs = item.companyJobs
        interviews = item.companyInterviews
        benefits = item.companyBenefits

        result = {
            'company_name': company_name,
            'overall_rating': overall_rating,
            'total_reviews': int(review),
            'recommend_to_friend': recommend_to_friend,
            'approve_of_ceo': approve_of_ceo,
            'jobs': jobs,
            'interviews': interviews,
            'benefits': benefits,
        }
        main_list.append(result)

    main_list = sorted(main_list, key=lambda j: j['total_reviews'], reverse=True)

    context = {
        'queryset': main_list,
    }

    return render(request, 'companies.html', context)


def multiplewords(request):
    qs = GlassdoorReview.objects.all()
    total = len(qs)
    search_word = request.GET.get('word')
    word_list = str(search_word).split(",")

    main_list = []
    company_and_total_review_list = []

    for item in qs:
        id = item.id
        url = item.companyUrl
        sub_main_list = []
        total_reviews = len(list(item.reviewDate.splitlines()))
        if total_reviews != 0:
            for word in word_list:
                company = item
                reviews_headings = company.reviewHeadings.replace('"', '').split()
                reviews_descriptions = company.reviewDescriptions.replace('"', '').split()
                reviews_pros = company.reviewPros.replace('"', '').split()
                reviews_cons = company.reviewCons.replace('"', '').split()

                total_count = 0
                for rev in reviews_headings:
                    if str(word) in rev.lower():
                        total_count += 1

                for rev in reviews_descriptions:
                    if str(word) in rev.lower():
                        total_count += 1

                for rev in reviews_pros:
                    if str(word) in rev.lower():
                        total_count += 1

                for rev in reviews_cons:
                    if str(word) in rev.lower():
                        total_count += 1

                sub_main_list.append(total_count)

            results = {
                'id': id,
                'company_url': url,
                'company_name': item.companyName,
                'total_reviews': total_reviews,
            }
            print(results["total_reviews"])
            company_and_total_review_list.append(results)

            main_list.append(sub_main_list)
        else:
            pass

    # list_to_show = sorted(list_to_show, key=lambda j: j['total_count'], reverse=True)
    # print(len(list_to_show))
    # for item in list_to_show:
    #     print(item)
    #
    mylist = zip(company_and_total_review_list, main_list)
    context = {
        'word': search_word,
        'word_list': word_list,
        'main_list': mylist,
    }

    return render(request, 'glassdoormultiplewords.html', context)


def reviewsInfo(request, pk):
    qs = GlassdoorReview.objects.get(pk=pk)
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
    pros = list(qs.reviewPros.splitlines())
    cons = list(qs.reviewCons.splitlines())
    headings = list(qs.reviewHeadings.splitlines())
    descriptions = list(qs.reviewDescriptions.splitlines())
    # print(date_list)
    # print(pros)
    # print(cons)
    # print(headings)
    # print(descriptions)

    reviews_headings = list(qs.reviewHeadings.replace('"', '').split())
    reviews_descriptions = list(qs.reviewDescriptions.replace('"', '').split())
    reviews_pros = list(qs.reviewPros.replace('"', '').split())
    reviews_cons = list(qs.reviewCons.replace('"', '').split())

    conditions = [
        word in reviews_headings,
        word in reviews_descriptions,
        word in reviews_pros,
        word in reviews_cons,
    ]

    total_reviews = len(date_list)
    for i in range(total_reviews):
        if search_word in headings[i] or word in descriptions[i] or word in pros or word in cons:
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
                "review_pros": pros[i],
                "review_cons": cons[i],
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

    return render(request, 'reviewinfo.html', context)


def test(request):
    return render(request, 'search.html')


def testtable(request):
    return render(request, 'glassdoor.html')


# Search Single word from both platforms
def singlewordboth(request):
    word = request.GET.get('word')
    glassdoordata = GlassdoorReview.objects.all()
    indeeddata = IndeedReview.objects.all()

    glassdoor_companies_list = []
    for item in glassdoordata:
        glassdoor_companies_list.append(item.companyName)

    indeed_companies_list = []
    for item in indeeddata:
        indeed_companies_list.append(item.companyName)

    glassdoor_companies_list = set(glassdoor_companies_list)
    common_companies_list = glassdoor_companies_list.intersection(indeed_companies_list)

    # List of common companies
    common_companies_list = list(common_companies_list)

    list_to_show = []
    for company in glassdoordata:
        if company.companyName in common_companies_list:
            reviews_headings = company.reviewHeadings.replace('"', '').split()
            reviews_descriptions = company.reviewDescriptions.replace('"', '').split()

            total_count = 0

            for rev_h in reviews_headings:
                if str(word) in rev_h.lower():
                    total_count += 1

            for rev_d in reviews_descriptions:
                if str(word) in rev_d.lower():
                    total_count += 1

            result_list = {
                'company_name': company.companyName,
                'word_count': total_count
            }
            list_to_show.append(result_list)

    for company in indeeddata:
        if company.companyName in common_companies_list:
            reviews_headings = company.reviewHeadings.replace('"', '').split()
            reviews_descriptions = company.reviewDescriptions.replace('"', '').split()

            index = next((count for (count, name) in enumerate(list_to_show) if name["company_name"] == company.companyName), None)

            for rev_h in reviews_headings:
                if str(word) in rev_h.lower():
                    list_to_show[index]['word_count'] += 1

            for rev_d in reviews_descriptions:
                if str(word) in rev_d.lower():
                    list_to_show[index]['word_count'] += 1

        list_to_show = sorted(list_to_show, key=lambda j: j['word_count'], reverse=True)

        context = {
            'word': word,
            'queryset': list_to_show,
        }

        return render(request, 'bothsingleword.html', context)
