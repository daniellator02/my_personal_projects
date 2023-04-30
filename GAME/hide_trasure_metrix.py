input("hide the treasure: press any botton to get started: ")
print("")

row1 = ["🌫","🌫","🌫"]
row2 = ["🌫","🌫","🌫"]
row3 = ["🌫","🌫","🌫"]
UNI_ROW = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print("")

navigator = input("Where do you want to put the treasure? ")
print("")
K1 = int(navigator[0])
K2 = int(navigator[1])

N1 = K1 - 1
N2 = K2 - 1
if N1 > 2 or N2 > 2:
  print("Dont go beyond 3")
else:
    UNI_ROW[N1][N2] = 'X'
    print(f"{UNI_ROW[0]}\n{UNI_ROW[1]}\n{UNI_ROW[2]}")
