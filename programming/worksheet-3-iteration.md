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
#### 2.
Python:
<br>
```{python}
number = 0
total = 0
tick = 0
repeat = True
while repeat == True:
  number = input("Enter your number (-1 to finish): ")
  if float(number) == -1:
    repeat = False
  else:
    tick += 1
    temp_total = float(total) + float(number)
    total = float(temp_total) / float(tick)
print(total)
```
### Task 3
#### a.
```
pendown()
FOR i <- 1 TO 4
forward(20)
right(90)
```
#### b.
```
pendown()
FOR i <- 1 TO 3
	FOR j <- 1 TO 4
		forward(20)
		right(90)
	ENDFOR
	penup()
	right(90)
	forward(20)
	right(90)
	forward(30)
ENDFOR
```
#### c.
```
pendown()
distance <- 10
FOR i <- 1 TO 7
	forward(distance)
	right(90)
	forward(distance)
	distance = distance + distance
ENDFOR
