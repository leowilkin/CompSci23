number = 0
total = 0
repeat = True
while repeat == True:
  number = input("Enter your number (-1 to finish): ")
  if int(number) == -1:
    repeat = False
  else:
    if int(number) >= 100:
      total += 1
print(total)
