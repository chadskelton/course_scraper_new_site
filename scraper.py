import scraperwiki
import time
from datetime import datetime
import smtplib
import requests
from BeautifulSoup import BeautifulSoup
# new for secret variables
import os
import mechanize

url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202030&startDatepicker=&endDatepicker=&uniqueSessionId=m403x1594404090223&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc"

html = requests.get(url)
htmlpage = html.content
soup = BeautifulSoup(htmlpage)

print soup
