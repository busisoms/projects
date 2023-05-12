# check if two strings are equal 

def check():
    string = input("Enter a string: ").lower()
    string2 = input("Enter a second string: ").lower()
    if string == string2:
        return True
    return False


ck = check()
print(ck)