# Worksheet 3 - Iteration

### Task 2
#### 1.
Python:
<br>
```{python}
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
```

Pseudocode:
<br>
```
Number <- 0
Total <- 0
Repeat <- True
WHILE repeat <- True
	Number <- INPUT user number
	IF number <- -1
		Repeat <- False
	ELSEIF
		IF number >= 100
			Total <- Total + 1
OUTPUT total
```
