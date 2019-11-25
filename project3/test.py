user_input = "testando top=10"
string = user_input.strip()
print(string)
print(len(string))

equal = string.find("=")
print(equal)

space_spot = string.find(" ")
print(space_spot)

first = string[:string.find(" ")]
print(first)
print(len(first))

second = string[string.find(" ") + 1:]
print(second)
print(len(second))