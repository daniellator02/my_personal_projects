print("Welcome to the love Calculator")
print(" ")
your_name = input("Enter your name: ")
their_name = input("Enter their name: ")
T = your_name + their_name
lets_match =T.lower() 


t = int(lets_match.count('t'))
r = int(lets_match.count('r'))
u = int(lets_match.count('u'))
e = int(lets_match.count('e'))
add_true = str(t + r + u + e)

l = int(lets_match.count('l'))
o = int(lets_match.count('o'))
v = int(lets_match.count('v'))
e = int(lets_match.count('e'))
add_love = str(l + o + v + e)

love_score = int(add_true + add_love)
if love_score < 10 or love_score > 90:
  print(f"Your score is %{love_score}, you go together like coke and mentos.")

elif love_score > 40 and love_score < 50:
  print(f"Your score is %{love_score}, you are alright together.")

else:
  print(f"Your score is %{love_score}.")

