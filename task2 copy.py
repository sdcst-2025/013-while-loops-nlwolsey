#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
correctUN = "admin"
correctPW = "12345password"
un = 0
pw = 0
while un != correctUN:
    while pw != correctPW:
        un = input("Enter username")
        if un == correctUN:
            pw = input("Enter password: ")
            if pw == correctPW:
                print("Access granted")
            else:
                print("Access denied")
        else:
            print("Access denied")
    
