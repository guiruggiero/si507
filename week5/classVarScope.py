
class MyClass:
  my_num = 5
  animals = ["dog", "cat"]
  def __init__(self):
  	pass
  	
object1 = MyClass()
object2 = MyClass()

print()
print()
print("Fist let's look at a number class variable")
print("MyClass.my_num is", MyClass.my_num, "and points to the address", id(MyClass.my_num))
print("object1.my_num is", object1.my_num, "and points to the address", id(object1.my_num))
print("object2.my_num is", object2.my_num, "and points to the address", id(object2.my_num))
print()

print("Adding 2 to MyClass.my_num...")
print("MyClass.my_num = MyClass.my_num + 2")
MyClass.my_num = MyClass.my_num + 2
print("MyClass.my_num is now", MyClass.my_num, "and points to the address", id(MyClass.my_num))
print("object1.my_num is", object1.my_num, "and points to the address", id(object1.my_num))
print("object2.my_num is", object2.my_num, "and points to the address", id(object2.my_num))
print()

print("multiplying object2.my_num by 2...")
print("object2.my_num = object2.my_num * 2")
object2.my_num = object2.my_num * 2
print("object2.my_num is now", object2.my_num, "and points to the address", id(object2.my_num))
print("object1.my_num is", object1.my_num, "and points to the address", id(object1.my_num))
print("MyClass.my_num is", MyClass.my_num, "and points to the address", id(MyClass.my_num))
print()
print()

print("now let's look at a list class variable")
print("MyClass.animals is", MyClass.animals, "and points to the address", id(MyClass.animals))
print("object1.animals is", object1.animals, "and points to the address", id(object1.animals))
print("object2.animals is", object2.animals, "and points to the address", id(object2.animals))
print()

print("appending 'cow' to the list via object1...")
print('object1.animals.append("cow")')
object1.animals.append("cow")
print("object1.animals is", object1.animals, "and points to the address", id(object1.animals))
print("object2.animals is", object2.animals, "and points to the address", id(object2.animals))
print("MyClass.animals is", MyClass.animals, "and points to the address", id(MyClass.animals))
print()

print("now, let's assign new content to object2.animals")
print('object2.animals = ["spider", "horse"]')
object2.animals = ["spider", "horse"]
print("object2.animals is now", object2.animals, "and points to the address", id(object2.animals))
print("object1.animals is", object1.animals, "and points to the address", id(object1.animals))
print("MyClass.animals is", MyClass.animals, "and points to the address", id(MyClass.animals))
print()

print("now let's assign new content to MyClass.animals")
print('MyClass.animals= ["sheep", "mice"]')
MyClass.animals= ["sheep", "mice"]
print("MyClass.animals is now", MyClass.animals, "and points to the address", id(MyClass.animals))
print("object1.animals is", object1.animals, "and points to the address", id(object1.animals))
print("object2.animals is", object2.animals, "and points to the address", id(object2.animals))
print()
