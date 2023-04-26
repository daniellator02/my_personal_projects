# Write your code below this line 
print('Welcome to the tip calculator.')
total = float(input('What was the total bill? $'))

per_tip = float(input('What percentage tip would you like to give? 10,12 or 15. '))

how_many_people = float(input('how many people to split the bills? '))
#lets perform small arithmetics 
p = per_tip / 100 
t = p * total
q = total + t
hmp = round(q / how_many_people, 2)
print(f"Each person should pay: ${hmp}")
