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

br = mechanize.Browser()
br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#List the forms
for form in br.forms():
    print "Form name:", form.name
    print form
