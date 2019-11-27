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

'''
bars ratings top=1
bars cocoa bottom=10
bars sellcountry=CA ratings top=5
bars sourceregion=Africa ratings top=5
companies region=Europe ratings top=5
companies country=US bars_sold top=5
companies cocoa top=5
countries sources ratings bottom=5
countries sellers bars_sold top=5
regions sources bars_sold top=5
regions sellers ratings top=10

-- 

bars ratings
bars sellcountry=US cocoa bottom=5
companies region=Europe bars_sold
companies ratings top=8
countries bars_sold
countries region=Asia ratings
regions bars_sold
regions ratings
bad command

bars nothing
'''