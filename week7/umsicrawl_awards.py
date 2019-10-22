import requests
from bs4 import BeautifulSoup

#next step would be simplify with a method
#def get_recipients(self, details_url):
#    return self.dic

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/news-events/awards-and-honors'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(catalog_url, headers=header).text
#print(page_text)
page_soup = BeautifulSoup(page_text, 'html.parser')
#print(page_soup)

#content_div = page_soup.find_all(class_='field field-name-body field-type-text-with-summary field-label-hidden')
#print(len(content_div)) #to see if there's more than one
content_div = page_soup.find(class_='field field-name-body field-type-text-with-summary field-label-hidden')
#print(content_div)

content_links = content_div.find_all('a')
#print(content_links)

margaret = {}
edmon = {}
john = {}
gary = {}

for a in content_links[:15]:
    #print(a)

    #print(a.text[:9])
    if a.text[:9] == "Margaret ":
        details_url_end = a['href']
        details_url = baseurl + details_url_end
        #print(details_url)

        page_text = requests.get(details_url, headers=header).text
        #print(page_text)
        page_soup = BeautifulSoup(page_text, 'html.parser')
        #print(page_soup)

        recipients_div = page_soup.find(class_='field field-name-body field-type-text-with-summary field-label-hidden')
        #print(recipients_div)
        recipients = recipients_div.find_all('p')
        #print(recipients)

        for p in recipients[3:]:
            #print(p.text)
            try:
                year = int(p.text[:4])
            except:
                year = p.text[:4]
            #print(year)
            recipient = p.text[4:]
            margaret[year] = recipient
        
        #print(margaret)

    elif a.text[:9] == "Edmon Low":
        details_url_end = a['href']
        details_url = baseurl + details_url_end
        #print(details_url)

        page_text = requests.get(details_url, headers=header).text
        page_soup = BeautifulSoup(page_text, 'html.parser')

        recipients_div = page_soup.find(class_='field field-name-body field-type-text-with-summary field-label-hidden')
        recipients = recipients_div.find_all('p')
        #print(recipients)

        for p in recipients[4:]:
            #print(p.text)
            try:
                year = int(p.text[-4:])
            except:
                year = p.text[-4:]
                #print(year)
            recipient = p.text[:-4]
            #print(recipient)
            edmon[year] = recipient
        
        #print(edmon)
    
    elif a.text[:9] == "John Lesl":
        details_url_end = a['href']
        details_url = baseurl + details_url_end
        #print(details_url)

        page_text = requests.get(details_url, headers=header).text
        page_soup = BeautifulSoup(page_text, 'html.parser')

        recipients_div = page_soup.find(class_='field field-name-body field-type-text-with-summary field-label-hidden')
        recipients = recipients_div.find_all('p')

        for p in recipients[2:]:
            #print(p.text)
            try:
                year = int(p.text[:4])
            except:
                year = p.text[:4]
            recipient = p.text[4:]
            john[year] = recipient

        #print(john)

    elif a.text[:9] == "The Gary ":
        details_url_end = a['href']
        details_url = baseurl + details_url_end
        #print(details_url)

        page_text = requests.get(details_url, headers=header).text
        page_soup = BeautifulSoup(page_text, 'html.parser')

        recipients_div = page_soup.find(class_='field field-name-body field-type-text-with-summary field-label-hidden')
        recipients = recipients_div.find_all('p')

        for p in recipients[4:]:
            #print(p.text)
            try:
                year = int(p.text[:4])
            except:
                year = p.text[:4]
            recipient = p.text[4:]
            gary[year] = recipient
        
        #print(gary)
    
    else:
        pass

print("2017:")
print("\tMargaret Mann Award:", margaret[2017])
print("\tEdmon Low Award:", edmon[2017])
print("\tJohn Leslie King Award:", john[2017])
print("\tThe Gary M. Olson Outstanding Ph.D. Student Award:", gary[2017])
print("2016:")
print("\tMargaret Mann Award:", margaret[2016])
print("\tEdmon Low Award:", edmon[2016])
print("\tJohn Leslie King Award:", john[2016])
print("\tThe Gary M. Olson Outstanding Ph.D. Student Award:", gary[2016])