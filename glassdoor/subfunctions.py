from .driverfile import *


def wait(t):
    time.sleep(t)


def login():
    driver.get('https://www.glassdoor.co.uk/index.htm')
    driver.maximize_window()
    print(driver.title)
    wait(20)
    driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()
    wait(20)
    username = driver.find_element_by_xpath('//*[@id="userEmail"]')
    password = driver.find_element_by_xpath('//*[@id="userPassword"]')
    wait(2)
    username.send_keys('sk0196146@gmail.com')
    wait(5)
    password.send_keys('P@ssw0rd9')
    wait(5)
    driver.find_element_by_xpath(
        '//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button').click()
    wait(20)
    print(driver.title)
    driver.get('https://www.glassdoor.com/Explore/top-companies-us_IL.14,16_IN1.htm')
    wait(15)
    print(driver.title)
