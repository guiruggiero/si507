SI 507 - Final project

Developed by Gui Ruggiero (gui@umich.edu)

Data sources used:
- public website ScubaEarth (https://www.scubaearth.com/). More specifically, it's dive site repository available to be searched on http://www.scubaearth.com/dive-site/dive-site-profile-search.aspx. A user can perform searches even without creating an account just by directly accessing the second link above
- CSV file containing my dive log - a detailed repository with information of all my dives. A user can access it just by opening the file on a spreadsheet app

How to run the program:
- run finalproject.py (it will run the others with user prompt)

--------------------------------------------------

Requirements/instructions:
- secret.py on the same folder with mapbox's access token attributed to the variable MAPBOX_TOKEN
- modules listed on requirements.txt
- chromedriver present as per instructions on https://chromedriver.chromium.org/getting-started

I have a Chromebook (runs Chrome OS, based on Linux) and Selenium was not very friendly in this somewhat different environment. Therefore, my final tests were (and the final presentation will be) done using UM's Virtual Sites - https://its.umich.edu/computing/computers-software/campus-computing-sites/virtual-sites. Here are the steps performed on the virtual machine to run the program:
1- copy chromedriver.exe, selenium_test.py, scubaearth.py, dives.csv, divelog.py, finalproject.py from K:\Academics\2019 Fall\SI 507\Final project to C:\Users\gui\Downloads
2- open VS Code via Chrome, folder, file, and install Python extension; close, and open VS Code
3- install latest Python from https://www.python.org/downloads/ (no admin privileges option)
4- run on terminal: C:\Users\gui\AppData\Local\Programs\Python\Python38-32\Scripts\pip3.exe install requests, bs4, selenium, csv, plotly
5- run C:\Users\gui\AppData\Local\Programs\Python\Python38-32\python.exe .\selenium_test.py to test
6- download DB Browser for SQLite (zip version) from https://sqlitebrowser.org/dl/ for demo
7- run C:\Users\gui\AppData\Local\Programs\Python\Python38-32\python.exe .\finalproject.py

--------------------------------------------------

Description of how the code is structured
- project is divided into part 1 ScubaEarth scraping with cache) and part 2 (import CSV), storing data from both parts on a database divelog.db
- part 1: contains the class Site, which has all the relevant information for a dive site. The trickiest part of this project, by far, was using Selenium to manipulate a browser window to insert search terms and click the search button (lines 71 to 93). Cache was implemented to reduce the load on the website while every result on the result page was crawled and scraped.
- part 2: contains the class Dive, which has some relevant information for a dive. Most important part here is data extraction from the CSV (lines 42 to 83). A nice feature is the visualization of the dives with geolocation data in a map (lines 160 to 182)