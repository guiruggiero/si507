# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

import scubaearth
import divelog

print("\n*** Welcome to Gui Ruggiero's final project ***\n")

response = input("What do you want me to run?\nOptions:\n"
    "   - 'part 1' (ScubaEarth scraping with cache and store in DB)\n"
    "   - 'part 2' (import CSV and store in DB)\n"
    "   - 'exit'\n\nYour option: ")

while response not in ["exit", "Exit", "quit", "Quit", "end", "End"]: 
    if response in ["part 1", "Part 1", "1", 1, "one", "One"]:
        print("\nAlright, running part 1\n")
        print("="*20 + " Part 1 " + "="*20 + "\n")
        scrape_scubaearth()
        print("*** That's it for part 1! ***\n")

    elif response in ["part 2", "Part 2", "2", 2, "two", "Two"]:
        print("\nNo problem, running part 2\n")
        print("="*20 + " Part 2 " + "="*20 + "\n")
        import_divelog_csv()
        print("*** Part 2 status: mission accomplished ***\n")

    else:
        print("\nI'm sorry, I did not understand your command. Try again, please?\n")

    response = input("What do you want me to run?\nOptions:\n"
        "   - 'part 1' (ScubaEarth scraping with cache and store in DB)\n"
        "   - 'part 2' (import CSV and store in DB)\n"
        "   - 'exit'\n\nYour option: ")

print("\n*** Final project done. C'est fini ***\n")
print("Teaching team, thank you for a great semester.  Happy holidays! :-)\n")