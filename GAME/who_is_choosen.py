import random

names_strings = input("Give me everybody's names, seperated by a comma: ").split()
names = names_strings
size = len(names)
ran = random.randint(0,size-1)

print(f"{names[ran]} is going to pay for the meal.")
