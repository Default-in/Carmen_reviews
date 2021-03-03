from django.shortcuts import render
from .models import IndeedReview
import csv
from django.http import HttpResponse


def download_csv_single_word(request, pk):
    qs = IndeedReview.objects.get(pk=pk)
    company_name = qs.companyName
    company_desc = qs.companyDesc
    word = request.GET.get('word')
    print(word)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={word}-{company_name}.csv'

    writer = csv.writer(response)
    writer.writerow(['Heading', 'Description'])


    list_to_show = []
    date_list = list(qs.reviewDate.splitlines())
    headings = list(qs.reviewHeadings.splitlines())
    descriptions = list(qs.reviewDescriptions.splitlines())

    total_reviews = len(date_list)
    for i in range(total_reviews):
        if word.lower() in headings[i].lower() or word.lower() in descriptions[i].lower():

            # result_list = {
            #     "review_date": date_list[i],
            #     "review_heading": headings[i],
            #     "review_descriptions": descriptions[i],
            # }
            writer.writerow([headings[i], descriptions[i]])

            # list_to_show.append(result_list)
        else:
            pass

    return response


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

    return render(request, 'indeed-single.html', context)


def reviewsInfo(request, pk):
    qs = IndeedReview.objects.get(pk=pk)
    company_name = qs.companyName
    company_desc = qs.companyDesc
    word = request.GET.get('word')
    print(word)

    list_to_show = []
    date_list = list(qs.reviewDate.splitlines())
    headings = list(qs.reviewHeadings.splitlines())
    descriptions = list(qs.reviewDescriptions.splitlines())

    total_reviews = len(date_list)
    for i in range(total_reviews):
        if word.lower() in headings[i].lower() or word.lower() in descriptions[i].lower():

            result_list = {
                "review_date": date_list[i],
                "review_heading": headings[i],
                "review_descriptions": descriptions[i],
            }

            list_to_show.append(result_list)
        else:
            pass

    context = {
        'company_name': company_name,
        'company_description': company_desc,
        'pk': pk,
        'queryset': list_to_show,
    }

    return render(request, 'indeed-reviews-info.html', context)


# Multiple Words
def multiplewords(request):
    qs = IndeedReview.objects.all()
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

                total_count = 0
                for rev in reviews_headings:
                    if str(word) in rev.lower():
                        total_count += 1

                for rev in reviews_descriptions:
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

    mylist = zip(company_and_total_review_list, main_list)
    context = {
        'word': search_word,
        'word_list': word_list,
        'main_list': mylist,
    }

    return render(request, 'indeed-multiple-words.html', context)


# Companies Info
def companyInfo(request):
    qs = IndeedReview.objects.all()

    main_list = []
    for item in qs:
        total_reviews = item.totalReviews
        review = ''
        for char in total_reviews:
            if char != 'K':
                review += char
            else:
                review = float(review) * 1000

        result = {
            'company_name': item.companyName,
            'overall_rating': item.overallRating,
            'work_life_balance': item.workLifeBalance,
            'pay_and_benefits': item.payAndBenefits,
            'job_security': item.jobSecurity,
            'management': item.management,
            'culture': item.culture,
            'total_reviews': int(review),
            'company_url': item.companyUrl,
        }
        main_list.append(result)

    main_list = sorted(main_list, key=lambda j: j['total_reviews'], reverse=True)

    context = {
        'queryset': main_list,
    }

    return render(request, 'indeed-companies.html', context)


# Both single and multiple words
def single_and_multiple_words(request):
    qs = IndeedReview.objects.all()
    total = len(qs)
    search_word = request.GET.get('word')
    word_list = str(search_word).split(",")

    if len(word_list) == 1:
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
                    if str(search_word).lower() in rev.lower():
                        total_heading += 1
                        total_count += 1

                for rev in reviews_descriptions:
                    if str(search_word).lower() in rev.lower():
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
            'word': search_word,
            'queryset': list_to_show,
        }

        return render(request, 'indeed-single.html', context)

    else:
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

                    total_count = 0
                    for rev in reviews_headings:
                        if str(word) in rev.lower():
                            total_count += 1

                    for rev in reviews_descriptions:
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

        mylist = zip(company_and_total_review_list, main_list)
        context = {
            'word': search_word,
            'word_list': word_list,
            'main_list': mylist,
        }

        return render(request, 'indeed-multiple-words.html', context)
