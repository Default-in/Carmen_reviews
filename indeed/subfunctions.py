import os
import time
from selenium import webdriver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
             "Safari/537.36 "

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.binary_location = binary_location
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
driver.implicitly_wait(10)


# Wait
def wait(t):
    time.sleep(t)


# Scroll till target
def scroll_till_target(target):
    driver.execute_script("arguments[0].scrollIntoView();", target)
    wait(2)


# Indeed login
def indeedLogin():
    driver.get('https://secure.indeed.com/account/login?hl=en_US&service=my&co=US&continue=https%3A%2F%2Fwww.indeed'
               '.com%2F')
    email = driver.find_element_by_xpath('//*[@id="login-email-input"]')
    for word in 'sk0196146@gmail.com':
        email.send_keys(word)
    password = driver.find_element_by_xpath('//*[@id="login-password-input"]')
    for word in 'P@ssw0rd9':
        password.send_keys(word)
    wait(30)
    driver.find_element_by_xpath('//*[@id="login-submit-button"]').click()
    wait(10)
