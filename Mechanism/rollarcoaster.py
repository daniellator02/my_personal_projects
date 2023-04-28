print("riding on a rollercoaster")

height = int(input("What's your height: "))
if height > 120:
  bill = 0
  print("You can ride")
  age = int(input("Enter your age: "))
  if 12 < age < 18:
    bill = 7
    print("Youth tickets are $7")

  elif age > 45 and age < 55:
    print("Your are eligible for free ride")    
    
  elif age >= 18:
    bill = 12
    print("Adult tickets are $12")
    
  else:
    bill = 5
    print("Child tickets are $5")
  pics = input("Do you want some photos? Y or N: ")
  if pics == 'Y':
    print("that would cost you additional $3")
    bill = bill + 3
    print(f"Your total bill is ${bill}")
  elif pics == 'N':
    print(f"Your total bill is ${bill}")
  else:
    print("Invalid entry, please start all over again and enter either Y or N")
  
  
    
else:
  print("Sorry you cant ride, wait till you are taller")

