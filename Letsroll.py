import random

answer = "Yes"
while answer == "Yes":
    print(random.randint(1,6))
    print("Would you like to roll again?")
    answer = raw_input("Yes or No")
