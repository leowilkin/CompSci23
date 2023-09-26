# Prep 3 - Iteration
## 1.
(a)
```
*
**
***
****
```
(b)
```
6 & 7
```
(c)
```
2 & 3
```
(d)
```
star <- 1
WHILE star < 10
  FOR n <- 1 TO star
    write("X")
  ENDFOR
  writeline // move to a new line
  star <- star + 2
ENDWHILE
```
## 2.
```
OUTPUT "Please enter number of temperatures (between 5 & 20): "
validNumber <- False
WHILE NOT validNumber
  numTemp <- STRING_TO_INT(USERINPUT)
  IF numTemp >= t AND numTemp <= 20 THEN
    validNumber <- True
  ELSE
    OUTPUT "Please enter a number between 5 & 20: "
  ENDIF
ENDWHILE
```
