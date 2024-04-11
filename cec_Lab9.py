#Colin Coppin
def encode(password):
    encodedpassword=""
    for digit in password:
        char=int(digit)
        char+=3
        if char>9:
            char=char%3
        encodedpassword+=str(char)
    return encodedpassword

def decode(password): # Decode Password Function - Added by Kevin Montero
    decoded_pass = "" # Initializes empty string to store decoded digits
    for digit in password: # Iterates through each digit in encoded password and shifts each number down by 3
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_pass += decoded_digit
    return decoded_pass # Returns Decoded Password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option=int(input("Please enter an option: "))
        if option==1:
            password=input("Please enter your password to encode: ")
            encodedpassword=encode(password)
            print("Your password has been encoded and stored!")
        elif option==2:
            password=input("Enter password to decode: ")
            password=decode(password)
            print(f"Your decoded password is {password}")
        elif option==3:
            break


if __name__=="__main__":
    main()