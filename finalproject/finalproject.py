# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

import classes
import scubaearth
import divelog

part1 = scrape_scubaearth()
if part1 == True:
    print("ScubaEarth scraped successfully\n")
else:
    print("There was a problem scraping ScubaEarth, please debug")

part2 = import_divelog_csv()
if part2 == True:
    print("Divelog CSV imported successfully\n")
else:
    print("There was a problem importing the divelog CSV, please debug")

if part1 == True and part2 == True:
    print("End of the final project. Happy holidays!")