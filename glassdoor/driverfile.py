import os
import time
from datetime import date
from selenium import webdriver


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
             "Safari/537.36 "

# driver_location = "/usr/bin/chromedriver"
# binary_location = "/usr/bin/google-chrome"
#
# options = webdriver.ChromeOptions()
# options.binary_location = binary_location
# options.add_argument(f'user-agent={user_agent}')
#
# driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument(f'user-agent={user_agent}')
op.add_argument("--window-size=1920,1080")
op.add_argument("--headless")
op.add_argument('--disable-dev-shm-usage')
op.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

print("Window size updated")

