from .subfunctions import *
from .models import *


# Reviews
def reviews():
    review_headings = ""
    review_dates = ""
    review_descriptions = ""
    review_pros = ""
    review_cons = ""
    try:
        for i in range(50):
            print(f"Page Number - {i+1}")
            try:
                for item in driver.find_elements_by_class_name('cmp-Review-moreButton'):
                    item.click()

            except Exception as exp:
                print(exp)

            for item in driver.find_elements_by_class_name('cmp-Review-content'):
                review_content = list(item.text.splitlines())
                length = len(review_content)
                review_headings += f'{review_content[0]}\n'
                review_dates += f'{review_content[1].split("-")[-1]}\n'
                review_descriptions += f'{review_content[2]}\n'

                # Pros and Cons
                try:
                    for i in range(length):
                        if review_content[i] == "Pros":
                            review_pros += f'{review_content[i + 1]}\n'

                        elif review_content[i] == "Cons":
                            review_cons += f'{review_content[i + 1]}\n'
                except Exception as ex:
                    print(ex)
                    review_pros += f" \n"
                    review_cons += f" \n"
            try:
                items = list(driver.find_elements_by_css_selector('a.icl-Button.icl-Button--tertiary.icl-Button--lg'))
                if items[-1].text == "Next":
                    items[-1].click()
                    print("Clicked")
                else:
                    break
            except Exception as expc:
                print(expc)
                break
            wait(5)
    except Exception as exp:
        print(exp)


    return review_headings, review_dates, review_descriptions, review_pros, review_cons





def indeed(name):
    driver.get('https://www.indeed.com/companies?from=gnav-homepage')
    driver.maximize_window()
    # Search company
    company = driver.find_element_by_xpath('//*[@id="exploreCompaniesWhat"]')
    company.send_keys(f'{name}')
    # Location
    location = driver.find_element_by_xpath('//*[@id="exploreCompaniesWhere"]')
    location.send_keys('United States')
    # Click on find companies button
    driver.find_element_by_xpath('//*[@id="exploreCompaniesSearchFormContainer"]/form/div[3]/button').click()
    # Click on first result
    driver.find_element_by_xpath('//*[@id="cmp-discovery"]/div[2]/div/div[2]/div/div[1]/div[2]/a[1]').click()
    company_name = driver.find_element_by_xpath(
        '//*[@id="cmp-container"]/div/div[1]/div[1]/div/header/div[2]/div[3]/div/div/div/div[1]/div[1]/div[2]/div['
        '1]/span').text
    print(company_name)
    try:
        company_desc = driver.find_element_by_xpath('//*[@id="cmp-Wonder-Section-About"]/div/section/div[3]/div/p').text
    except Exception as e:
        print(e)
        company_desc = ""

    company_url = driver.current_url
    # Click on Reviews Button
    driver.find_element_by_xpath('//*[@id="cmp-skip-header-desktop"]/div/ul/li[3]/a').click()
    total_reviews = driver.find_element_by_xpath('//*[@id="cmp-skip-header-desktop"]/div/ul/li[3]/a/div').text
    print(total_reviews)
    overall_rating = driver.find_element_by_class_name('cmp-CompactHeaderCompanyRatings-value').text
    print(overall_rating)
    ratings = []
    for item in driver.find_elements_by_class_name('cmp-TopicFilter-rating'):
        ratings.append(item.text)

    try:
        work_life_balance = ratings[0]
        print(work_life_balance)
        pay_and_benefits = ratings[1]
        print(pay_and_benefits)
        job_security = ratings[2]
        print(job_security)
        management = ratings[3]
        print(management)
        culture = ratings[4]
        print(culture)
    except Exception as ex:
        print(ex)
        work_life_balance = ""
        pay_and_benefits = ""
        job_security = ""
        management = ""
        culture = ""

    headings, dates, descriptions, pros, cons = reviews()

    IndeedReview.objects.create(
        companyName=company_name,
        companyDesc=company_desc,
        overallRating=overall_rating,
        totalReviews=total_reviews,
        workLifeBalance=work_life_balance,
        payAndBenefits=pay_and_benefits,
        jobSecurity=job_security,
        management=management,
        culture=culture,
        reviewHeadings=headings,
        reviewDescriptions=descriptions,
        reviewPros=pros,
        reviewCons=cons,
        reviewDate=dates,
        companyUrl=company_url,
    )
    print("Success")

