#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""
var1= 1
var2= 1
list = [1,1]
s=0
while s<100:
    s= var1+var2 
    var1=var2
    var2=s
    if s<100:
        list.append (s)
print (list)
