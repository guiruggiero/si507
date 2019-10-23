# 507 Homework 7 Part 1
# Developed by Gui Ruggiero

import requests
import json
from bs4 import BeautifulSoup

# Trying to load the cache from file
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# If no file, create a dictionary
except:
    CACHE_DICTION = {}

# Main cache function
def make_request_using_cache(url):
    unique_ident = url

    # Data already in cache?
    if unique_ident in CACHE_DICTION:
        #print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    # No - fetch data and add it to cache
    else:
        #print("Making a request for new data...")
        resp = requests.get(url, headers={'User-Agent': 'SI_CLASS'})
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

#### Your Part 1 solution goes here ####

def get_umsi_data(page):
    for i in range(0,14):
        # Creating dictionary
        umsi_people = {}
        
        # Accessing and parsing page of the directory
        url_complement = "&page=" + str(i)
        #print(url_complement)
        #print(page + url_complement)
        page_text = make_request_using_cache(page + url_complement)
        #print(page_text)
        page_soup = BeautifulSoup(page_text, 'html.parser')
        #print(page_soup)
        
        # Finding div where links to contact derails are
        content_div = page_soup.find(class_="view-content")
        #print(content_div)
        links = content_div.find_all('a')
        #print(links)

        # Going through every UMSI person on the page
        for link in links:
            #print(link.text)
            if link.text == "Contact Details":

                # Accessing and parsing profile page
                details_url_end = link['href']
                #print(details_url_end)
                #print("https://www.si.umich.edu" + details_url_end)
                details_page_text = make_request_using_cache("https://www.si.umich.edu" + details_url_end)
                #print(details_page_text)
                details_page_soup = BeautifulSoup(details_page_text, 'html.parser')
                #print(details_page_soup)

                # Finding div where information is and storing information
                details_div = details_page_soup.find(id="content")
                name = details_div.find("h2").text
                #print(name)
                email = details_div.find("a").text
                #print(email)
                title_div = details_div.find(class_="field field-name-field-person-titles field-type-text field-label-hidden")
                #print(title_div)
                title = title_div.find(class_="field-item even").text
                #print(title)

                # Writing to dictionary
                #print(email, "-", name + ",", title)
                umsi_people[email] = {'name': name, 'title': title}
        
    #print(umsi_people)
    return umsi_people

#### Execute function, get_umsi_data, here ####
url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All"
umsi_people = get_umsi_data(url)
#print(umsi_people)

#### Write out file here #####
json = json.dumps(umsi_people)
f = open("directory_dict.json", "w")
f.write(json)
f.close()
print("\nFile 'directory_dict.json' successfully created!\n")