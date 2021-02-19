from .models import GlassdoorReview
from django.shortcuts import render


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
            for rev in reviews_headings:
                if str(word) in rev.lower():
                    total_heading += 1
                    total_count += 1

            for rev in reviews_descriptions:
                if str(word) in rev.lower():
                    total_desc += 1
                    total_count += 1

            for rev in reviews_pros:
                if str(word) in rev.lower():
                    total_pros += 1
                    total_count += 1

            for rev in reviews_cons:
                if str(word) in rev.lower():
                    total_cons += 1
                    total_count += 1

            result_list = {
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
    for item in list_to_show:
        print(item)

    context = {
        'queryset': list_to_show,
    }

    return render(request, 'table.html', context)


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
        'word_list': word_list,
        'main_list': mylist,
    }

    return render(request, 'multipleWords.html', context)
