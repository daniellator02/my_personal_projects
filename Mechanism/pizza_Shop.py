print("Welcome to your python pizza😏")
print(" ")

size = input("What size of pizza do you want?. S,M or L: ")
bill = 0
if size == 'S':
  bill = 15
  Pepperoni = input("Do you want Pepperoni? Y or N: ")
  if Pepperoni == 'Y':
    bill = bill + 2
    Extra = input("Do you want extra cheese? Y or N: ")
    if Extra == 'Y':
      bill = bill + 1
      print(f"Your final bill is: ${bill}.") 
    elif Extra == 'N':  
      print(f"Your final bill is: ${bill}. ")    
  elif Pepperoni == 'N':
    Extra = input("Do you want extra cheese? Y or N ")
    if Extra == 'Y':
      bill = bill + 1
      print(f"Your final bill is: ${bill}. ")
    elif Extra == 'N':
      print(f"Your final bill is: ${bill}. ")
      
    
elif size == 'M':
  bill = 20
  Pepperoni = input("Do you want Pepperoni? Y or N: ")
  if Pepperoni == 'Y':
    bill = bill + 3
    Extra = input("Do you want extra cheese? Y or N: ")
    if Extra == 'Y':
       bill = bill + 1
       print(f"Your final bill is: ${bill}.")
    elif Extra == 'N':
      print(f"Your final bill is: ${bill}. ")
  elif Pepperoni == 'N':
    Extra = input("Do you want extra cheese? Y or N: ")
    if Extra == 'Y':
      bill = bill + 1
      print(f"Your final bill is: ${bill}. ")
    elif Extra == 'N':
      print(f"Your final bill is: ${bill}. ")
 
elif size == 'L':
  bill = 25
  Pepperoni = input("Do you want Pepperoni? Y or N: ")
  if Pepperoni == 'Y':
    bill = bill + 3  
    Extra = input("Do you want extra cheese? Y or N: ")
    if Extra == 'Y':
      bill = bill + 1
      print(f"Your final bill is: ${bill}.")
    elif Extra == 'N':
      print(f"Your final bill is: ${bill}. ")
  elif Pepperoni == 'N':
    Extra = input("Do you want extra cheese? Y or N: ")
    if Extra == 'Y':
      bill = bill + 1
      print(f"Your final bill is: ${bill}. ")
    elif Extra == 'N':
      print(f"Your final bill is: ${bill}. ")
else:
  print("Ivalid entry, please start all over again and enter either S, M or L")
