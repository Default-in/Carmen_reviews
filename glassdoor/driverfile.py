import os
from selenium import webdriver

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
#              "Safari/537.36 "
#
# driver_location = "/usr/bin/chromedriver"
# binary_location = "/usr/bin/google-chrome"
#
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.binary_location = binary_location
# options.add_argument(f'user-agent={user_agent}')
#
# driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
#
# print("Window size updated")


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
             "Safari/537.36 "

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
