import colorama

def int_input(prompt, min_lenght = None, max_lenght = None):

    while True:

        number = input(prompt).strip()

        if not number:
            print("This field cannot be empty !")
            continue

        try:
            number = int(number)
        except ValueError:
            print("Please enter a number !")
            continue

        if min_lenght is not None and min_lenght > number:
            print(f"Must be at least {min_lenght}.")

        if max_lenght is not None and max_lenght < number:
            print(f"Must be at most {max_lenght}.")

        return number

def text_input(prompt, allowed_answers=None):
    """
    Safely asks the user for text input.
    - Ensures the input contains only alphabetic characters.
    - If allowed_answers is provided, input must match one of them.
    """
    while True:
        answer = input(prompt).lower().strip()

        if not answer:
            print("This field cannot be empty.")
            continue

        if not answer.isalpha():
            print("Please enter a valid text input!")
            continue

        if allowed_answers and answer not in allowed_answers:
            print(f"Please enter only: {', '.join(allowed_answers)}")
            continue

        return answer
    
def yes_no(prompt):
    
    while True:
        
        answer = input(prompt).strip().lower()

        if not answer:
            print("This field cannot be empty.")
            continue

        if answer in ("yes","y"):
            return True
        
        if answer in ("no","n"):
            return False
        

        print("Please enter only 'yes/y' or 'no/n' !")


        

