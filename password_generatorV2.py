import random
import time
from Utilities import int_input, yes_no
from Utilities import Color



def character_group():

    lower_cases = "abcdefghijklmnopqrstuvwxyz"
    upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symboles = "!@#$%^&*()-_=+[]{};:,.?/"

    return lower_cases, upper_cases,numbers,symboles

def password_properties():

    password_lenght = int_input("Please enter your password lenght (must be 6-30) = ", min_lenght=6, max_lenght=30)

    use_upper = yes_no("Do you want it to contain upper characters? (y/n)")

    use_lower = yes_no("Do you want it to contain lower characters? (y/n)")

    use_number = yes_no("Do you want it to contain numbers? (y/n)")

    use_symbole = yes_no("Do you want it to contain symbols? (y/n)")

    how_many_password = int_input("How many password do you want to generate = ", min_lenght=1, max_lenght=10)

    return password_lenght,use_upper,use_lower,use_number,use_symbole,how_many_password

def main():

    print("Welcome to our password generator !")
    generate_again = True

    while generate_again:

        lower_cases, upper_cases, numbers, symboles = character_group() ## CALLING VARIABLES

        password_lenght, use_upper, use_lower, use_number, use_symbole, how_many_password = password_properties() ## CALLING VARIABLES

## ------------------ MAKING A PASSWORD POOL HERE BY USERS CHOICE --------------------- ##
        password_pool = ""

        if use_upper:
            password_pool += upper_cases

        if use_lower:
            password_pool += lower_cases
        
        if use_number:
            password_pool += numbers

        if use_symbole:
            password_pool += symboles
## -------------------------------------------------------------------- ##

## ------------------ GENERATING PASSWORD HERE --------------------- ##

        generated_passwords  = []
        new_password = ""

        for _ in range(how_many_password):

            for _ in range(password_lenght):

                new_password += random.choice(password_pool)

            generated_passwords.append(new_password)
            new_password = ""
        
        print("Here is your passwords : ")
        for x in generated_passwords:
            Color.green(f"- {x} ")


## ## ----------------------- AGAIN ? ------------------------- ##

        time.sleep(2)

        choice = yes_no("Do you want to generate again ? (y/n) : ")

        if not choice:
            Color.yellow("Thank you for using our program :)")
            generate_again = False
  

if __name__ == "__main__":
    main()



