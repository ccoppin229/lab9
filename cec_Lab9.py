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
def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option=int(input("Please enter an option: "))
        if option==1:
            password=input("Please enter your password to encode: ")
            encodedpassword=encode(password)
            print("Your password has been encoded and stored!")
        elif option==2:
            pass
        elif option==3:
            break


if __name__=="__main__":
    main()