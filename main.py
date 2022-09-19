# If you want to scarp a website:
# 1. use the API
# HTML Web Scraping using some tool like bs4

# step 0:  Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://google.co.in"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# STep 2: parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
# Step 3: HTML Tree traversal