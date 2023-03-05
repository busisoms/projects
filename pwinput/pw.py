
"""----------------How i would create a simple login system------------------"""

from pwinput import pwinput
print('Create Login details')
# Promote user to create login details

usern = input("Enter username: ")
pwd = pwinput("Create Password: ")
# ensure that the password is 8 charaters or more
if not len(pwd) >= 8:
    print('Password has to be 8 charaters')
    quit()
# quit the program if condition not met
c_pwd = pwinput("Confirm password: ")
if pwd == c_pwd:
    print("Done")
else:
    print("password doesn't match, try again")
    quit()
print("Now sign-in")

# Promote user to sign-in
# print("sign-in")
while True:
    usern2 = input("Username: ")
    passw = pwinput("Password: ", "*")
    if passw == pwd and usern2 == usern:
        print(F"welcome back {usern}")
        break
    else:
        print("try again")
# print("Done")
