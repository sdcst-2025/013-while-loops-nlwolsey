##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
username="admin"
pwd= "12345"
attempt=0
while attempt < 3:
    user= input("Enter username:")
    password= input("Enter password:")
    attempt = attempt + 1 
    if user==username and password==pwd:
        print ("Access Granted") 
    else: 
        print ("Try Again.")

print ("Too many failed attempts")


