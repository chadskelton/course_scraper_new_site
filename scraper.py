#!/usr/bin/env python

# Load in modules
# !!! NOTE - When doing a more general News Bot, should probably create another field that describes the data
# (i.e. "New Court Decision") and one that has the email of the person to notify (as this may vary depending
# on the site scraped. Could then have one script grabbing dozens of different sites and notifying
# dozens of different reporters/editors !!!

import scraperwiki
import tweepy
import time
from datetime import datetime
import smtplib
import requests
from BeautifulSoup import BeautifulSoup
# new for secret variables
import os
import mechanize

s = requests.Session()

payload = {'term': '202030'} # term selection

browser={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

html = s.get("https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search", verify=False, headers=browser) # just trying to mimic what browser does

print BeautifulSoup(html.content)

print ' PAGE 2 '

html = s.post("https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search", verify=False, data=payload, allow_redirects=True, headers=browser) # trying post

print BeautifulSoup (html.content)

'''

s.get("https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/selfServiceMenu/data", verify=False, headers=browser) # just trying to mimic what browser does

s. get("https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/classSearch/getTerms?searchTerm=202030&offset=1&max=1", verify=False, headers=browser)

html = s.post("https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search", verify=False, data=payload, allow_redirects=True, headers=browser) # trying post

# htmlpage = html.content

# soup = BeautifulSoup(htmlpage)

# print soup


url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/classSearch/classSearch"

html = s.get(url, verify=False, headers=browser)

url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202030&startDatepicker=&endDatepicker=&uniqueSessionId=1ckwm1594421672965&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc"

html = s.get(url, verify=False, headers=browser)

htmlpage = html.content

soup = BeautifulSoup(htmlpage)

print soup

'''
