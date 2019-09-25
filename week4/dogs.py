class Dog:
  large_dogs = ['German Shepherd', 'Golden Retriever',
          'Rottweiler', 'Collie',
          'Mastiff', 'Great Dane']
  small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
          'Beagle', 'Dachshund', 'Shih Tzu']

  def __init__(self, nm, br):
    self.name = nm
    self.breed = br

  def speak(self):
    if self.breed in self.large_dogs:
      print('woof')
    elif self.breed in self.small_dogs:
      print('yip')
    else:
      print('rrrrr')

d1 = Dog('Fido', 'German Shepherd')
d2 = Dog('Rufus', 'Lhasa Apso')
d3 = Dog('Fred', 'Mutt')

dogs = [d1, d2, d3]
for d in dogs:
    print(d.name, "says ", end = '') 
    d.speak()

print("\n")
# print(Dog.large_dogs)
# print(d1.large_dogs)
d1.large_dogs.append('Doberman')
print(d3.large_dogs)