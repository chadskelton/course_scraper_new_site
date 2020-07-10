#!/usr/bin/env python

# Scraping new site

import mechanize 
import lxml.html
import time
import urllib2
import scraperwiki
from datetime import datetime
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')]

url = "https://banweb3.kpu.ca/StudentRegistrationSsb/ssb/term/termSelection?mode=search"

response = br.open(url, timeout=60)

print response.read()

br.select_form(nr=0) # selects first form on the page
        
for f in br.forms(): # these two lines show the form elements
	print f

'''
departments = ['ACCT', 'ACUP', 'AGRI', 'ANTH', 'CMNS', 'APSC', 'ARTH', 'ARTS', 'ASIA', 'ASTR', 'BIOL', 'BIOQ', 'HOPS', 'BUSI', 'BUSM', 'BUQU', 'CHEM', 'CHEQ', 'CADA', 'CADM', 'COMM', 'CBSY', 'CPSC', 'CADD', 'COOP', 'CNPS', 'CRWR', 'CRIM', 'ECON', 'EDAS', 'EDUC', 'ENGL', 'ELST', 'ELSQ', 'ENGQ', 'ENTR', 'ENVI', 'EXCH', 'FASN', 'FMRK', 'FNSR', 'FINA', 'FIND', 'FREN', 'GEOG', 'GNIE', 'GNQU', 'GDMA', 'GRMT', 'HCAP', 'HSCI', 'HEAL', 'HIST', 'HORT', 'HRMT', 'INDG', 'INFO', 'IDEA', 'IDSN', 'IBUS', 'JAPN', 'JRNL', 'LANC', 'LGLA', 'LING', 'MAND', 'MRKT', 'MATQ', 'MATH', 'MAMT', 'MUSI', 'NRSG', 'OSCM', 'PHIL', 'PHYS', 'PHYQ', 'POST', 'POLI', 'DEPD', 'PSYN', 'PSYC', 'PRLN', 'PUNJ', 'WRTG', 'SOCI', 'SPAN', 'DETA', 'TMAS', 'ZZZZ', 'WELD']

for department in departments:
    
    try:

        # url = "https://bweb.kwantlen.ca/pls/prodss/bwysched.p_select_term?wsea_code=ACAD"
        # Invalid security certificate seems to be due to URL switching from kwantlen.ca to kpu.ca
        # Old kwantlen.ca site is still there but security certificate is invalid because it's tied to kpu.ca
        
        url = "https://bweb.kpu.ca/pls/prodss/bwysched.p_select_term?wsea_code=ACAD"
        
        response = br.open(url, timeout=60)
        
        # response = br.open(url)
        
        # print response.read()
        
        # br.form = list(br.forms())[0]
        
        br.select_form(nr=0) # selects first form on the page
        
        for f in br.forms(): # these two lines show the form elements
            print f
        
        # br.form['term_code'] = '201520'
        
        br.form.set_all_readonly(False) # allow changing the .value of all controls
        
        name = ['202030',] # this is actual term code, should change this each term; will be 201530 for Fall 2015; need to change dummy below too
        
        for control in br.form.controls:
            if control.name == 'term_code':
                control.value = name
                name = '201920' # this is dummy term code, but seems to change (was 201510; not 201530); check POST form fields; doesn't seem to matter
        
        response = br.submit()
        
        html = response.read()
        
        # print html
        
        br.select_form(nr=0)
        
        for f in br.forms(): # these two lines show the form elements
            print f
        
        br.form.set_all_readonly(False) # allow changing the .value of all controls
        
        name = 'dummy'
        
        for control in br.form.controls:
            if control.name == 'sel_subj':
                control.value = name
                name = [department]
        
        response = br.submit()
        
        html = response.read()
        
        # print html
        
        
        soup = BeautifulSoup(html)
                
        tables = soup.findAll("table", {"class" : "dataentrytable"})
        
        print 'Here are the tables'
        
        rows = soup.findAll("tr")
        
        for row in rows:
            
            cells = row.findAll("td")
            
            try:
                if "checkbox" in str(cells[0]):
                    
                    print 'NEW ROW'
                    
                    record = {}
                    record["department"] = department
                    record["uniqueid"] = str(datetime.now())
                    record["course"] = cells[1].text
                    record["CRN"] = cells[2].text
                    record["title"] = cells[3].text
                    record["credits"] = cells[4].text
                    record["campus"] = cells[5].text
                    record["instructor"] = cells[6].text
                    record["link"] = cells[7].text
                    record["max"] = cells[9].text
                    record["enrolled"] = cells[10].text
                    record["available"] = cells[11].text
                    record["waitlisted"] = cells[12].text
                    
                    print record
                    
                    scraperwiki.sqlite.save(['CRN'], record, table_name="data") # this should overwrite the CRN; if want discrete time entries should do it on uniqueid
                    scraperwiki.sqlite.save(['uniqueid'], record, table_name="overtime") # this should save, in a separate table, a new entry for every time it searches
                    
                else:
                    print 'No course data in this row'
                        
            except:
                print 'No course data in this row*'

    except:
        print "*** Didn't work for Department: " + department + " ***"

'''

'''
print tables[1]
for table[1] in tables:
    print table
'''  
