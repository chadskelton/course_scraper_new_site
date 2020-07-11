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

url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search"

payload = {'term': '202030'} # term selection

html = s.get(url, verify=False) # get first

html = s.post(url, verify=False, data=payload) # trying post

htmlpage = html.content

soup = BeautifulSoup(htmlpage)

print soup

url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/classSearch/classSearch"

htmlpage = html.content

soup = BeautifulSoup(htmlpage)

print soup

html = s.get(url, verify=False)

url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202030&startDatepicker=&endDatepicker=&uniqueSessionId=1ckwm1594421672965&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc"

html = s.get(url, verify=False)

htmlpage = html.content

soup = BeautifulSoup(htmlpage)

print soup
