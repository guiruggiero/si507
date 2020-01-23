# SI 507 Fall 2019
# Homework 3

# Developed by Gui Ruggiero and Aditya Iyer

import random

def get_question():
    question = input("\nPlease, write your question: ")
    return question

def validate_question(question):
	if question == "quit" or question == "Quit":
		print("Thanks for playing. Bye!\n")
		quit()
	elif question.endswith("?"):
		validation = True
	else:
		validation = False
		print("This is not a question, try again or type 'quit' to stop playing.")
	return validation

def give_response():
	responses = [
		"It is certain.",
		"It is decidedly so.",
		"Without a doubt.",
		"Yes - definitely.",
		"You may rely on it.",
		"As I see it, yes.",
		"Most likely.",
		"Outlook good.",
		"Yes.",
		"Signs point to yes.",
		"Reply hazy, try again.",
		"Ask again later.",
		"Better not tell you now.",
		"Cannot predict now.",
		"Concentrate and ask again.",
		"Don't count on it.",
		"My reply is no.",
		"My sources say no.",
		"Outlook not so good.",
	    "Very doubtful."
	]
	i = random.randint(0,len(responses)-1)
	j= responses[i]
	print (j, "\n")

if __name__ == "__main__":
	question = ""
	while question != "quit" and question != "Quit":
		question = get_question()
		validation = validate_question(question)
		if validation == True:
			give_response()
			quit()