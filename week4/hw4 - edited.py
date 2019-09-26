'''
SI 507 F19 homework 4: Classes and Inheritance

Developed by: Gui Ruggiero
Your discussion section: 3
People you worked with: Caitlin Endyke

######### DO NOT CHANGE PROVIDED CODE ############ 
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

import random

'''
Task A
'''

from random import randrange

class Explore_pet:

    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

coco = Explore_pet()

print()
brian = Explore_pet("Brian")
brian.hunger = 11
print(brian, "\n")

'''
Task B
'''

class Pet:

    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.words = ["hello"]

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state
    
    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2
    
    def say(self, all_mode = True):
        if all_mode == True:
            print("I know how to say: ")
            for a in self.words:
                print(a)
        else:
            return random.choice(self.words)
    
    def teach(self, word):
        self.words.append(word)
        if -self.boredom_decrement > self.boredom:
            self.boredom = 0
        else:
            self.boredom += self.boredom_decrement
    
    def feed(self):
        if -self.hunger_decrement > self.hunger:
            self.hunger = 0
        else:
            self.hunger += self.hunger_decrement
    
    def hi(self):
        print(self.say(False))

'''
Task C
'''

def teaching_session(my_pet, new_words):

    for a in new_words:
        my_pet.teach(a)
        my_pet.hi()
        print(my_pet)
        if my_pet.mood() == "hungry":
            my_pet.feed()
        my_pet.clock_tick()

tina = Pet("Tina")
teaching_session(tina, ["I am sleepy", "You are the best", "I love you, too"])
print()

#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################

'''
Task A: Dog and Cat    
'''

class Dog(Pet):

    def __str__(self):
        state = "I'm " + self.name + ", arrrf! "
        state += 'I feel ' + self.mood() + ", arrrf! "
        if self.mood() == 'hungry':
            state += "Feed me, arrrf!"
        if self.mood() == 'bored':
            state += "You can teach me new words, arrrf!"
        return state

class Cat(Pet):

    def __init__(self, name = "Coco", meow_count = 1):
        self.meow_count = meow_count
        super().__init__(name)

    def hi(self):
        phrase = ""
        word = self.say(False)
        i = 0
        while i < self.meow_count:
            phrase += word
            i += 1
        print(phrase)

'''
Task B: Poodle 
'''

class Poodle(Dog):

    def dance(self):
        print("Dancing in circles like poodles do!")
    
    def say(self, all_mode = True):
        self.dance()
        print(super().say(False))

fluflu = Poodle("Fluflu")
fluflu.say(False)
print()

garfield = Cat("Garfield", 5)
garfield.hi()
print()