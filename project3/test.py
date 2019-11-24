user_input = "testando agora"
string = user_input.strip()
print(string)
print(len(string))

space_spot = string.find(" ")
print(space_spot)

first = string[:string.find(" ")]
print(first)
print(len(first))

second = string[string.find(" ") + 1:]
print(second)
print(len(second))