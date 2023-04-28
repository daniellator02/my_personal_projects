print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
A = input("which direction? left or right: ")
if A == 'right':
  print("walk straight towards the hill and search for the key: ")
  B = input("Climb the hill: climb or go back: ")
  if B == 'climb':
    print("when you get to the top of the hill follow the dragon's footprint.")
    print(" ")
    print("Good job, You have gotten to the island, defeat the dragon to claim the treasures.")
    print(" ")

    C = input("do you want to fight the dragon? yes or no: ")
    if C == 'yes':
      D = input("choose your weapon, Gun or magic sword? ")
      if D == 'magic sword':
        E = input("strike his heart or strike other part? ")
        if E == 'strike his heart':
          F = input("wow you have killed the dragon, now claim treasure, yes or no? ")
          if F == 'yes':
            print("you have won, hurry!")

          elif F == 'no':
            print('game over, too sad you gave up easily')      

        elif E == 'strike other body parts':
          print("Game over")          

        elif D == 'Gun':
          print("Game over")     

    elif C == 'no':
      print("Game over")
    
  elif B == 'go back':
    print("Game over")

elif A == 'left':
  print("Game over")

else:
  print("Game over")
