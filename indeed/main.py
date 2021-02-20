from .functions import *
from .companies import *
from .subfunctions import indeedLogin

# login to indeed
indeedLogin()

# Go to companies
for company in companies_list:
    indeed(company)
