import random

input = input("select one rock,paper,scissors 1 or 2 or 3 ")

list = ['rock', 'paper', 'scissors']
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
select = random.choice(list)

print("PC Select")
print(globals()[select])
if (input == "1" and select == "rock"):
    print(rock)
    print("equal,no win")


elif (input == "2" and select == "paper"):
    print(paper)
    print("equal,no win")


elif (input == "3" and select == "scissors"):
    print(scissors)
    print("equal,no win")


elif (input ==" 1" and select == "paper"):
    print(rock)
    print("you are game over")

elif (input == "1" and select == "scissors"):
    print(rock)
    print("you win")

elif (input == "2" and select == "rock"):
    print(paper)
    print("you win")

elif (input == "2" and select == "scissors"):
    print(paper)
    print("you are game over  ")

elif (input == "3" and select == "rock"):
    print(scissors)
    print("you are game over")

elif(input=="3" and select=="paper"):
    print(scissors)
    print("you win")



