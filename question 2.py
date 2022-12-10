import requests
from bs4 import BeautifulSoup
import re

url = input("Enter website url: ")
r = requests.get(url)
sm_sites = ['twitter.com','facebook.com','linkedin.com','instagram.com']
sm_sites_present = []

soup = BeautifulSoup(r.content, 'html5lib')
all_links = soup.find_all('a', href = True)

print("\n"+"Socail links -")
for sm_site in sm_sites:
    for link in all_links:
        if sm_site in link.attrs['href']:
            print(link.attrs['href'])

phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?
                        (\s|-|\.)
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)

# Create email id regular expression
email_regex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

        
page_html = str(r.content)        
        
matches = []
matches1 = []

for groups in email_regex.findall(page_html):
    matches1.append(groups[0])

print("\n"+"Email/s-")
l1 = [*set(matches1)]        
print('\n'.join(l1))

for groups in phone_regex.findall(page_html):
    phone_numbers = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_numbers += ' x' + groups[8]            
    matches.append(phone_numbers)  
     
print("\n"+"Contact:")              
l = [*set(matches)]        
print('\n'.join(l))

print("\n")
        

