from .subfunctions import *
from .models import *
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
from .mail import *
from .glassdoor_cookies import *


# Def scrap companies name and reviews url and store them in database
def scrap_companies_name_and_review_page_url():
    driver.get(
        'https://www.glassdoor.com/Explore/browse-companies.htm?overall_rating_low=3.5&page=1&isHiringSurge=0&locId=1&locType=N&locName=US&occ=Technology&countryPickerRedirect=true')

    wait(60)
    for i in range(102, 200):
        try:
            if i > 5:
                main_list = []
                company_names = []
                for item in driver.find_elements_by_css_selector('span.align-items-center.mb-xsm'):
                    company_names.append(item.text.splitlines()[0])

                company_links = []
                for j in range(len(company_names)):
                    link = driver.find_element_by_xpath(
                        f'//*[@id="ReactCompanyExplorePageContainer"]/div/div/div/div/div[2]/section[{j + 1}]/div/div[2]/a[1]').get_attribute(
                        'href')
                    company_links.append(link)

                for k in range(len(company_names)):
                    sub_dict = {
                        'company_name': f'{company_names[k]}',
                        'company_url': f'{company_links[k]}'
                    }
                    main_list.append(sub_dict)

                for item in main_list:
                    GlassdoorCompanies.objects.create(
                        companyName=item['company_name'],
                        companyReviewPageUrl=item['company_url']
                    )
                print(f"Added {len(company_names)} companies data into models")

            print("Go to next page")
            for item in driver.find_elements_by_css_selector('li.pagination__PaginationStyles__inner.d-inline-block'):
                if str(item.text) == f'{i + 1}':
                    item.click()
                    wait(10)
                else:
                    pass


        except Exception as ex:
            print(ex)


# Reviews scrap
def review_scrapped(n):
    dates = ""
    headings = ""
    descriptions = ""
    pros = ""
    cons = ""
    reviews_employees_rating = ""
    try:
        for i in range(1, n + 1):
            print(f'Page number - {i}')

            # Click on continue reading
            try:
                for item in driver.find_elements_by_class_name('v2__EIReviewDetailsV2__continueReading'):
                    item.click()
            except Exception as continue_button_exception:
                print("Unable to click on continue reading button", continue_button_exception)

            date_of_review = ""
            review_heading = ""
            review_desc = ""
            review_pros = ""
            review_cons = ""
            employee_rating = ''
            try:
                print("reviews")
                for rev in driver.find_elements_by_class_name('gdReview'):
                    review = list(rev.text.splitlines())
                    date_of_review = review[0]

                    if valid_review(date_of_review):
                        try:
                            if review[1].split(" ")[0].lower() != 'helpful':
                                review_heading = review[1]
                                employee_rating = review[2]

                                for j in range(len(review)):
                                    if review[j] == 'Pros':
                                        review_desc = review[j - 1]
                                        review_pros = review[j + 1]
                                        review_cons = review[j + 3]

                                # if review[7] == 'No Opinion of CEO' or review[7] == 'Approves of CEO' or review[
                                #     7] == 'Disapproves of CEO':
                                #     review_desc = review[8]
                                #     review_pros = review[10]
                                #     review_cons = review[12]
                                #
                                # elif (review[6] == 'Positive Outlook' or review[6] == 'No Opinion of CEO' or review[
                                #     6] == 'Approves of CEO' or review[6] == 'Disapproves of CEO' or review[
                                #           6] == 'Neutral Outlook' or review[6] == 'Negative Outlook') and \
                                #         (review[7] != 'No Opinion of CEO' or review[7] != 'Approves of CEO' or review[
                                #             7] != 'Disapproves of CEO'):
                                #     review_desc = review[7]
                                #     review_pros = review[9]
                                #     review_cons = review[11]
                                # elif (review[5] == 'Recommends' or review[5] == 'Positive Outlook' or review[
                                #     5] == 'No Opinion of CEO' or review[5] == 'Approves of CEO' or review[
                                #           5] == "Doesn't Recommend" or review[5] == 'Neutral Outlook' or review[
                                #           5] == 'Negative Outlook' or review[5] == 'Disapproves of CEO') and \
                                #         (review[6] == 'Positive Outlook' or review[6] == 'No Opinion of CEO' or review[
                                #             6] == 'Approves of CEO' or review[6] == 'Disapproves of CEO' or review[
                                #              6] == 'Neutral Outlook' or review[6] == 'Negative Outlook'):
                                #     review_desc = review[6]
                                #     review_pros = review[8]
                                #     review_cons = review[10]
                                #
                                # else:
                                #     review_desc = review[5]
                                #     review_pros = review[7]
                                #     review_cons = review[9]

                                # Now adding
                                # dates += f'{date_of_review}\n'
                                # headings += f'{review_heading}\n'
                                # descriptions += f'{review_desc}\n'
                                # pros += f'{review_pros}\n'
                                # cons += f'{review_cons}\n'

                            else:
                                review_heading = review[2]
                                employee_rating = review[3]
                                for j in range(len(review)):
                                    if review[j] == 'Pros':
                                        review_desc = review[j - 1]
                                        review_pros = review[j + 1]
                                        review_cons = review[j + 3]
                                # if review[8] == 'No Opinion of CEO' or review[8] == 'Approves of CEO' or review[
                                #     8] == 'Disapproves of CEO':
                                #     review_desc = review[9]
                                #     review_pros = review[11]
                                #     review_cons = review[13]
                                #
                                # elif (review[7] == 'Positive Outlook' or review[7] == 'No Opinion of CEO' or review[
                                #     7] == 'Approves of CEO' or review[7] == 'Disapproves of CEO' or review[
                                #           7] == 'Neutral Outlook' or review[7] == 'Negative Outlook') and \
                                #         (review[8] != 'No Opinion of CEO' or review[8] != 'Approves of CEO' or review[
                                #             8] != 'Disapproves of CEO'):
                                #     review_desc = review[8]
                                #     review_pros = review[10]
                                #     review_cons = review[12]
                                # elif (review[6] == 'Recommends' or review[6] == 'Positive Outlook' or review[
                                #     6] == 'No Opinion of CEO' or review[6] == 'Approves of CEO' or review[
                                #           6] == "Doesn't Recommend" or review[6] == 'Neutral Outlook' or review[
                                #           6] == 'Negative Outlook' or review[6] == 'Disapproves of CEO') and \
                                #         (review[7] == 'Positive Outlook' or review[7] == 'No Opinion of CEO' or review[
                                #             7] == 'Approves of CEO' or review[7] == 'Disapproves of CEO' or review[
                                #              7] == 'Neutral Outlook' or review[7] == 'Negative Outlook'):
                                #     review_desc = review[7]
                                #     review_pros = review[9]
                                #     review_cons = review[11]
                                #
                                # else:
                                #     review_desc = review[6]
                                #     review_pros = review[8]
                                #     review_cons = review[10]

                                # Now adding
                                # dates += f'{date_of_review}\n'
                                # headings += f'{review_heading}\n'
                                # descriptions += f'{review_desc}\n'
                                # pros += f'{review_pros}\n'
                                # cons += f'{review_cons}\n'
                        except Exception as exp:
                            print(exp)
                    else:
                        print("6 months older review so coming out of loop")
                        return dates, headings, descriptions, pros, cons, reviews_employees_rating


            except Exception as ex:
                print(ex)

            # Now adding
            dates += f'{date_of_review}\n'
            headings += f'{review_heading}\n'
            descriptions += f'{review_desc}\n'
            pros += f'{review_pros}\n'
            cons += f'{review_cons}\n'
            reviews_employees_rating += f'{employee_rating}\n'

            # next Page
            for item in driver.find_elements_by_css_selector('button.page.css-sed91k'):
                if str(item.text) == f'{i+1}':
                    item.click()
                    wait(8)
                    break

    except Exception as exp:
        print(f'Exception in Reviews - {exp}')

    return dates, headings, descriptions, pros, cons, reviews_employees_rating


# Scrapped data
def scrap_data():
    try:
        i = 1
        while i < 11:
            wait(5)
            if i != 11:
                try:
                    target = driver.find_element_by_xpath(f'//*[@id="ReactCompanyExplorePageContainer"]/div/div/div'
                                                          f'/div[2]/div[2]/section[{i}]/div/div[1]/div/div[2]/span/h2')
                    scroll_till_target(target)
                    target.click()
                    wait(5)
                except:
                    target = driver.find_element_by_xpath(f'//*[@id="ReactCompanyExplorePageContainer"]/div/div/div'
                                                          f'/div/div[2]/section[{i}]/div/div[1]/div/div[2]/span/h2')
                    scroll_till_target(target)
                    target.click()
                    wait(5)
                base_window = driver.window_handles[0]
                print(driver.window_handles)
                # Switch to companies window
                driver.switch_to.window(driver.window_handles[1])
                # wait(10)
                try:
                    company_name = driver.find_element_by_xpath('//*[@id="DivisionsDropdownComponent"]').text
                    print(company_name)
                    total_reviews = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[1]/span[1]').text
                    print(total_reviews)
                    jobs = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[2]/span[1]').text
                    print(jobs)
                    interviews = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[4]/span[1]').text
                    print(interviews)
                    benefits = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[5]/span[1]').text
                    print(benefits)
                    # Company url
                    job_url = driver.current_url
                except:
                    company_name = ''
                    total_reviews = ''
                    jobs = ''
                    interviews = ''
                    benefits = ''
                    job_url = ''
                try:
                    # Read more button
                    driver.find_element_by_xpath('//*[@id="EIOverviewContainer"]/div/div[1]/div[1]/span/button').click()
                    wait(2)
                    # Company Description
                    company_desc = driver.find_element_by_xpath(
                        '//*[@id="EIOverviewContainer"]/div/div[1]/div/span').text
                    print(company_desc)
                except Exception as ex:
                    print(ex)
                    company_desc = ''
                # Click on Reviews
                driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[1]').click()
                wait(2)
                try:
                    # OverAll Rating
                    overall_rating = driver.find_element_by_xpath('//*[@id="EmpStats"]/div/div[1]/div/div/div').text
                    print(overall_rating)
                except:
                    overall_rating = ''
                # Other ratings
                j = 1
                recommend_to_friend = ''
                approve_of_ceo = ''
                for rating in driver.find_elements_by_class_name('donut__DonutStyle__donutchart_text_val'):
                    if j == 1:
                        recommend_to_friend = rating.text
                        print(recommend_to_friend)
                    elif j == 2:
                        approve_of_ceo = rating.text
                        print(approve_of_ceo)
                    else:
                        break
                    j += 1

                try:
                    # Click on more pros and cons
                    driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/span').click()
                    wait(2)
                    # Pros of company
                    pros = driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/div[1]/div[1]/ul').text
                    # Cons of company
                    cons = driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/div[1]/div[2]/ul').text
                except:
                    pros = " "
                    cons = ' '

                # Reviews
                reviews_dates, reviews_headings, reviews_decriptions, reviews_pros, reviews_cons = review_scrapped(1)

                GlassdoorReview.objects.create(
                    companyName=company_name,
                    companyDesc=company_desc,
                    companyJobs=jobs,
                    companyInterviews=interviews,
                    companyBenefits=benefits,
                    overallRating=overall_rating,
                    totalReviews=total_reviews,
                    recommendToFriend=recommend_to_friend,
                    approveOfCEO=approve_of_ceo,
                    overallPros=pros,
                    overallCons=cons,
                    reviewHeadings=reviews_headings,
                    reviewDescriptions=reviews_decriptions,
                    reviewPros=reviews_pros,
                    reviewCons=reviews_cons,
                    reviewDate=reviews_dates,
                    companyUrl=job_url,
                )
                print("Success")

            else:
                pass
            # Go to the companies page
            wait(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            wait(2)
            i += 1
    except Exception as ex:
        print(ex)


def companies(i):
    j = 13
    print("Start")
    try:
        while j < 100:
            print(f'Page Number - {j}')
            try:
                scrap_data()
            except Exception as ex:
                print(ex)

            driver.close()

            # driver.find_element_by_xpath(
            #     '//*[@id="ReactCompanyExplorePageContainer"]/div/div/div/div/div[3]/div/ul/li[7]/button').click()
            # wait(20)
            # j += 1

    except Exception as ex:
        print(ex)


# Click on overview page
def overview_page():
    target = driver.find_element_by_css_selector('span.eiCell.cell.overviews.switchLogo')
    hover = ActionChains(driver).move_to_element(target)
    hover.perform()
    driver.find_element_by_xpath('//*[@id="HierarchiesDropdown"]/div/a[1]').click()


# Recent 6 months reviews are valid
def valid_review(review_date):
    valid = True

    # test_string = 'Mar 22, 2021 - Junior Trader'

    try:
        review_date = review_date.split('-')[0].strip().split()

        today_date = date.today()
        today_date = str(today_date).split('-')

        try:
            d0 = date(int(review_date[2]), month_string_to_number(review_date[0]), int(review_date[1].replace(',', '')))
        except:
            d0 = date(int(review_date[2]), month_string_to_number(review_date[1]), int(review_date[0]))
        d1 = date(int(today_date[0]), int(today_date[1]), int(today_date[2]))
        delta = d1 - d0
        diff = delta.days

        if diff > 183:
            valid = False
    except:
        pass

    return valid


# Another design reviews scrapper
# n is the number of pages of reviews we want to scrap. Glassdoor show 10 review per page
def different_design_review_scrapper(n):
    reviews_dates = ""
    reviews_headings = ""
    reviews_descriptions = ""
    reviews_pros = ""
    reviews_cons = ""
    reviews_employees_rating = ""

    for page_no in range(1, n + 1):
        print(f'Page Number - {page_no}')

        try:
            # Click on all continue reading button
            i = 1
            for item in driver.find_elements_by_css_selector(
                    'p.mt-0.mb-0.pb.v2__EIReviewDetailsV2__bodyColor.v2__EIReviewDetailsV2__lineHeightLarge.v2__EIReviewDetailsV2__isCollapsed  '):
                if i % 2 == 0:
                    item.click()
                i += 1
        except:
            print("Error while clicking continue read button")

        try:
            for review in driver.find_elements_by_css_selector(
                    'div.p-0.mb-0.mb-md-std.css-w5wad1.gd-ui-module.css-1qsvfgq'):
                review = review.text.splitlines()
                review_date = review[4]

                # check whether review valid or not
                if valid_review(review_date):
                    employee_review_date = review_date.split('-')[0].strip()
                    employee_rating = review[0]
                    review_heading = review[3]
                    review_pros = review[9]
                    review_cons = review[11]

                    # append all these review parts in main list
                    reviews_dates += f'{employee_review_date}\n'
                    reviews_headings += f'{review_heading}\n'
                    reviews_pros += f'{review_pros}\n'
                    reviews_cons += f'{review_cons}\n'
                    reviews_employees_rating += f'{employee_rating}\n'

                # If review is older than 6 month then stop scraping
                else:
                    return reviews_dates, reviews_headings, reviews_descriptions, reviews_pros, reviews_cons, reviews_employees_rating

                # Click on next page
                for item in driver.find_elements_by_css_selector('button.page.css-sed91k'):
                    if str(item.text) == f'{page_no + 1}':
                        item.click()
                        wait(8)
                        break

        except Exception as ex:
            print(ex)

    return reviews_dates, reviews_headings, reviews_descriptions, reviews_pros, reviews_cons, reviews_employees_rating


# This function will get companies url and name from database and compare it already store companies data if company
# name is not present then scrap reviews for those companies.
# n is the count of companies whose data we want to scrap
def scrap_companies_reviews(n, m):
    already_store_companies = GlassdoorReview.objects.all()
    companies_review_page_urls_and_names = GlassdoorCompanies.objects.all()

    already_store_companies_names = [item.companyName for item in already_store_companies]
    # print(already_store_companies_names)

    for company in companies_review_page_urls_and_names:
        company_name = company.companyName

        if str(company_name) not in already_store_companies_names and n != 0:
            print(company_name)
            review_page_url = company.companyReviewPageUrl
            print(review_page_url)
            driver.get(review_page_url)
            print("-------------------")
            n -= 1
            print(f'Value of n left - {n}')

            try:

                # Total reviews of companies
                total_reviews = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[1]/span[1]').text
                print(total_reviews)

                # Total jobs
                jobs = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[2]/span[1]').text
                print(jobs)

                # Total Interviews
                interviews = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[4]/span[1]').text
                print(interviews)

                # Total benefits
                benefits = driver.find_element_by_xpath('//*[@id="EIProductHeaders"]/div/a[5]/span[1]').text
                print(benefits)

                # overall rating
                overall_rating = driver.find_element_by_css_selector(
                    'div.v2__EIReviewsRatingsStylesV2__ratingNum.v2__EIReviewsRatingsStylesV2__large').text
                print(overall_rating)
            except:
                print("Error while scraping data of jobs or interviews etc")
                total_reviews = ''
                jobs = ''
                interviews = ''
                benefits = ''
                overall_rating = ''

            # Other ratings
            j = 1
            recommend_to_friend = ''
            approve_of_ceo = ''
            try:
                for rating in driver.find_elements_by_class_name('donut__DonutStyle__donutchart_text_val'):
                    if j == 1:
                        recommend_to_friend = rating.text
                        print(recommend_to_friend)
                    elif j == 2:
                        approve_of_ceo = rating.text
                        print(approve_of_ceo)
                    else:
                        break
                    j += 1
            except:
                pass

            # Overall pros and cons
            try:
                wait(2)
                more_pros_and_cons_button = driver.find_element_by_css_selector('span.link.minor.d-flex.align-items-center.strong')
                # scroll_till_target(more_pros_and_cons_button)
                more_pros_and_cons_button.click()
                pros = driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/div[1]/div[1]/div').text
                cons = driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/div[1]/div[2]/div').text

                print("Start review scraping from 2nd design")
                # scrap reviews of m number of pages
                reviews_dates, reviews_headings, reviews_decriptions, reviews_pros, reviews_cons, employees_ratings = different_design_review_scrapper(m)

                try:
                    # Click on overview page
                    overview_page()

                    # Scrap company description
                    company_desc = ''
                    try:
                        for div in driver.find_elements_by_css_selector('div.my-std.css-1w9mklt.e16x8fv01'):
                            company_desc = div.text
                            break
                    except Exception as exp:
                        print(exp)
                except Exception as overview_page_error:
                    print(overview_page_error)
                    company_desc = ''

            except Exception as ex:
                print("Another design")
                print(ex)

                wait(2)
                # Click on more pros and cons
                target = driver.find_element_by_css_selector('span.link.minor')
                # scroll_till_target(target)
                target.click()
                # Overall Pros of company
                pros = driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/div[1]/div[1]/ul').text
                # Overall Cons of company
                cons = driver.find_element_by_xpath('//*[@id="ReviewHighlightsModule"]/div[1]/div[2]/ul').text

                print("Start review scraping")
                # scrap reviews of m number of pages
                reviews_dates, reviews_headings, reviews_decriptions, reviews_pros, reviews_cons, employees_ratings = review_scrapped(m)

                # Go to overview page
                overview_page()

                try:
                    driver.find_element_by_xpath('//*[@id="EIOverviewContainer"]/div/div[1]/div[1]/span/button').click()
                    company_desc = driver.find_element_by_xpath('//*[@id="EIOverviewContainer"]/div/div[1]/div/span').text
                except:
                    company_desc = ''

            # Company overview page url
            company_url = driver.current_url

            GlassdoorReview.objects.create(
                companyName=company_name,
                companyDesc=company_desc,
                companyJobs=jobs,
                companyInterviews=interviews,
                companyBenefits=benefits,
                overallRating=overall_rating,
                totalReviews=total_reviews,
                recommendToFriend=recommend_to_friend,
                approveOfCEO=approve_of_ceo,
                overallPros=pros,
                overallCons=cons,
                reviewHeadings=reviews_headings,
                reviewDescriptions=reviews_decriptions,
                reviewPros=reviews_pros,
                reviewCons=reviews_cons,
                reviewDate=reviews_dates,
                employeesRatings=employees_ratings,
                companyUrl=company_url,
            )
            print("Success")


        elif n == 0:
            break
