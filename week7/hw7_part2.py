# 507 Homework 7 Part 2
# Developed by Gui Ruggiero

import json

count = 0

#### Your Part 2 solution goes here ####

# Reading file and storing content in a dictionary
dictionary_file = open("directory_dict.json", 'r')
dictionary_content = dictionary_file.read()
#print(dictionary_content)
umsi_people = json.loads(dictionary_content)
#print(umsi_people)
dictionary_file.close()

for person in umsi_people:
    #print(umsi_people[person]['title'])
    if umsi_people[person]['title'] == "PhD student":
        count += 1

#### Your answer output (change the value in the variable, count)####
print('The number of PhD students: ', count)