# 507 Homework 7 Part 2
# Developed by Gui Ruggiero

count = 0
#### Your Part 2 solution goes here ####

# Reading file and storing content in a dictionary
dictionary_file = open("directory_dict.json", 'r')
dictionary_content = dictionary_file.read()
umsi_people = json.loads(dictionary_content)
dictionary_file.close()

i = 0
for person in umsi_people:
    #print(person)
    #print(person[i])
    #print(person["title"])
    #print(person[i]["title"])
    if person[i]["title"] == "PhD student":
        count += 1

#### Your answer output (change the value in the variable, count)####
print('The number of PhD students: ', count)