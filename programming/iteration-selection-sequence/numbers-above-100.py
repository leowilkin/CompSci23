Number = 0
Total = 0
No_Number = input("Enter the number of numbers you want to enter: ")
for i in range(0, int(No_Number)):
  Number = input("Enter your number: ")
  if int(Number) >= 100:
    Total += 1
print(Total)
