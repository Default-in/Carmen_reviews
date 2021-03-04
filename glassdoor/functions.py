from .subfunctions import *
from .models import *
from .mail import *
from .glassdoor_cookies import *


def login():
    try:
        driver.get('https://www.glassdoor.com/index.htm')
        wait(30)
        driver.maximize_window()
        print(driver.title)
        # wait(10)
        driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()
        username = driver.find_element_by_xpath('//*[@id="userEmail"]')
        password = driver.find_element_by_xpath('//*[@id="userPassword"]')
        wait(2)
        username.send_keys('sk0196146@gmail.com')
        wait(2)
        password.send_keys('P@ssw0rd9')
        wait(2)
        sign_in = driver.find_element_by_xpath(
            '//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button')
        sign_in.click()
        wait(10)
        driver.get(
            'https://www.glassdoor.com/Explore/browse-companies.htm?overall_rating_low=3.5&page=14&isHiringSurge=0'
            '&locId=1&locType=N&locName=US')
        wait(45)

    except Exception as e:
        print(e)
        driver.find_element_by_xpath('//*[@id="SiteNav"]/nav/div[2]/div/div/div/button').click()
        username = driver.find_element_by_xpath('//*[@id="userEmail"]')
        password = driver.find_element_by_xpath('//*[@id="userPassword"]')
        wait(2)
        username.send_keys('sk0196146@gmail.com')
        wait(2)
        password.send_keys('P@ssw0rd9')
        wait(2)
        sign_in = driver.find_element_by_xpath(
            '//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button')
        sign_in.click()
        wait(10)
        driver.get(
            'https://www.glassdoor.com/Explore/browse-companies.htm?overall_rating_low=3.5&page=14&isHiringSurge=0'
            '&locId=1&locType=N&locName=US')
        wait(15)


# Reviews scrap
def review_scrapped(j):
    i = j
    dates = ""
    headings = ""
    descriptions = ""
    pros = ""
    cons = ""
    try:
        while i != 101:
            print(f'Page number - {i}')
            wait(1)
            # Click on continue reading
            try:
                for item in driver.find_elements_by_class_name('v2__EIReviewDetailsV2__continueReading'):
                    wait(1)
                    item.click()
            except:
                print("Unable to click on continue reading button")

            try:
                print("reviews")
                for rev in driver.find_elements_by_class_name('gdReview'):
                    date_of_review = ""
                    review_heading = ""
                    review_desc = ""
                    review_pros = ""
                    review_cons = ""
                    review = list(rev.text.splitlines())
                    date_of_review = review[0]

                    if review[1].split(" ")[0].lower() != 'helpful':
                        review_heading = review[1]
                        if review[7] == 'No Opinion of CEO' or review[7] == 'Approves of CEO' or review[
                            7] == 'Disapproves of CEO':
                            review_desc = review[8]
                            review_pros = review[10]
                            review_cons = review[12]

                        elif (review[6] == 'Positive Outlook' or review[6] == 'No Opinion of CEO' or review[
                            6] == 'Approves of CEO' or review[6] == 'Disapproves of CEO' or review[
                                  6] == 'Neutral Outlook' or review[6] == 'Negative Outlook') and \
                                (review[7] != 'No Opinion of CEO' or review[7] != 'Approves of CEO' or review[
                                    7] != 'Disapproves of CEO'):
                            review_desc = review[7]
                            review_pros = review[9]
                            review_cons = review[11]
                        elif (review[5] == 'Recommends' or review[5] == 'Positive Outlook' or review[
                            5] == 'No Opinion of CEO' or review[5] == 'Approves of CEO' or review[
                                  5] == "Doesn't Recommend" or review[5] == 'Neutral Outlook' or review[
                                  5] == 'Negative Outlook' or review[5] == 'Disapproves of CEO') and \
                                (review[6] == 'Positive Outlook' or review[6] == 'No Opinion of CEO' or review[
                                    6] == 'Approves of CEO' or review[6] == 'Disapproves of CEO' or review[
                                     6] == 'Neutral Outlook' or review[6] == 'Negative Outlook'):
                            review_desc = review[6]
                            review_pros = review[8]
                            review_cons = review[10]

                        else:
                            review_desc = review[5]
                            review_pros = review[7]
                            review_cons = review[9]

                        # Now adding
                        dates += f'{date_of_review}\n'
                        headings += f'{review_heading}\n'
                        descriptions += f'{review_desc}\n'
                        pros += f'{review_pros}\n'
                        cons += f'{review_cons}\n'

                    else:
                        review_heading = review[2]
                        if review[8] == 'No Opinion of CEO' or review[8] == 'Approves of CEO' or review[
                            8] == 'Disapproves of CEO':
                            review_desc = review[9]
                            review_pros = review[11]
                            review_cons = review[13]

                        elif (review[7] == 'Positive Outlook' or review[7] == 'No Opinion of CEO' or review[
                            7] == 'Approves of CEO' or review[7] == 'Disapproves of CEO' or review[
                                  7] == 'Neutral Outlook' or review[7] == 'Negative Outlook') and \
                                (review[8] != 'No Opinion of CEO' or review[8] != 'Approves of CEO' or review[
                                    8] != 'Disapproves of CEO'):
                            review_desc = review[8]
                            review_pros = review[10]
                            review_cons = review[12]
                        elif (review[6] == 'Recommends' or review[6] == 'Positive Outlook' or review[
                            6] == 'No Opinion of CEO' or review[6] == 'Approves of CEO' or review[
                                  6] == "Doesn't Recommend" or review[6] == 'Neutral Outlook' or review[
                                  6] == 'Negative Outlook' or review[6] == 'Disapproves of CEO') and \
                                (review[7] == 'Positive Outlook' or review[7] == 'No Opinion of CEO' or review[
                                    7] == 'Approves of CEO' or review[7] == 'Disapproves of CEO' or review[
                                     7] == 'Neutral Outlook' or review[7] == 'Negative Outlook'):
                            review_desc = review[7]
                            review_pros = review[9]
                            review_cons = review[11]

                        else:
                            review_desc = review[6]
                            review_pros = review[8]
                            review_cons = review[10]

                        # Now adding
                        dates += f'{date_of_review}\n'
                        headings += f'{review_heading}\n'
                        descriptions += f'{review_desc}\n'
                        pros += f'{review_pros}\n'
                        cons += f'{review_cons}\n'


            except Exception as ex:
                print(ex)
                date_of_review = ""
                review_heading = ""
                review_desc = ""
                review_pros = ""
                review_cons = ""

                # Now adding
                dates += f'{date_of_review}\n'
                headings += f'{review_heading}\n'
                descriptions += f'{review_desc}\n'
                pros += f'{review_pros}\n'
                cons += f'{review_cons}\n'

            if i == 1:
                driver.find_element_by_xpath(
                    '//*[@id="NodeReplace"]/main/div/div[1]/div/div[8]/div/div[1]/button[7]').click()
                wait(1)
            else:
                driver.find_element_by_xpath(
                    '//*[@id="NodeReplace"]/main/div/div[1]/div/div[7]/div/div[1]/button[7]').click()
                wait(1)
            i += 1
    except Exception as exp:
        print(f'Exception in Reviews - {exp}')


    return dates, headings, descriptions, pros, cons


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
