import random

name = "PJ"
question = "Are you a newb?"
answer = ""
random_number = random.randint(1, 9)

if (random_number == 1):
    answer = print("Yes - definitely")
elif (random_number == 2):
    answer = print("It is decidedly so")
elif (random_number == 3):
    answer = print("Without a doubt")
elif (random_number == 4):
    answer = print("Reply hazy, try again")
elif (random_number == 5):
    answer = print("Ask again later")
elif (random_number == 6):
    answer = print("Better not tell you now")
elif (random_number == 7):
    answer = print("My sources say no")
elif (random_number == 8):
    answer = print("Outlook not so good")
elif (random_number == 9):
    answer = print("Very doubtful")
else:
    answer = print("Error")

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)