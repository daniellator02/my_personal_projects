print("Welcome to the leap year detector")
year = int(input("Enter a Year: "))

if year % 4 == 0:
  if year % 100 == 0: 
    if year % 400 == 0:
      print("its a leap year")
    else:
      print("Not a leap year") 
  else:
    print("its a leap year")
else:
  print("Not a leap year")
