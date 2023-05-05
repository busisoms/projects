# Password generating program
def pass_length():
    while True:
        try:
            length = int(input("how long do you want your password to be: "))
            if length > 13 or length < 5:
                print("password has to be between 5 and 13")
            else:
                return length
        except:
            print("Invalid entry, please enter a number")


def upper_or_lower():
    while True:
        try:
            uol = input(
                "Should the password be lower or upper case (L/U): ").upper()
            if uol == "L" or uol == "U":
                return uol
        except:
            print('please enter "U" for upper case or "L" for lower case')


def generate(length):
    import random as r
    import string
    characters = string.ascii_letters + string.digits
    random_key = r.sample(characters, length)
    return random_key


if __name__ == "__main__":
    hl = pass_length()
    case = upper_or_lower()
    randomize = generate(hl)
    if case == "L":
        final = ''.join(randomize)
        print(f"Here is your password:{final.lower()}")
    else:
        case == "U"
        final = ''.join(randomize)
        print(f"Here is your password: {final.upper()}")
