import requests
import json
from bs4 import BeautifulSoup

# On startup, try to load the cache from file
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# If there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}

# The main cache function: it will always return the result for this url.
# However, it will first look to see if we have already cached the result
# and, if so, return the result from cache. If we haven't cached the
# result, it will get a new one (and cache it)
def make_request_using_cache(url, header):
    unique_ident = url

    # First, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    # If not, fetch the data afresh, add it to the cache,
    # then write the cache to file
    else:
        print("Making a request for new data...")
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

#next step would be simplify with a method
#def get_recipients(self, details_url):
#    return self.dic

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/news-events/awards-and-honors'
header = {'User-Agent': 'SI_CLASS'}
page_text = make_request_using_cache(catalog_url, header)
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

        page_text = make_request_using_cache(details_url, header)
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

        page_text = make_request_using_cache(details_url, header)
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

        page_text = make_request_using_cache(details_url, header)
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

        page_text = make_request_using_cache(details_url, header)
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