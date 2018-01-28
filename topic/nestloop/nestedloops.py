#!/usr/bin/python
i = 0
import pudb; pu.db
while(i < 10):
    j = 2
    while(j <= (i/j)):
        if not(i%j):
            break
        j = j + 1
    if (j > i/j) :
        print(i, " is prime")
    else:
        print(i ," is not prime")
    i = i + 1
print("Good bye!")
