
class Pet:
    def __init__(self, name="Coco", y=["hello"]):
        self.name = name
        self.words = y.copy()

    def teach(self, word):
        self.words.append(word)


def teaching_session(mypet, new_words):
    for each_word in new_words:
        mypet.teach(each_word)


print("a pet")
a=Pet()
teaching_session(a, ['I am sleepy', 'You are the best'])
print(a.words)
print(id(a.words))
print(a.name)
print(id(a.name))
a.name="chloe"
print(id(a.name))

print("\n")
print("b pet")
b=Pet()
print(b.name)
print(b.words)  #it prints ["hello", "I am sleepy", "you are the best"]
print(id(b.words))
print(b.name)
print(id(b.name))
