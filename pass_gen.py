import random

"""
Author: Harivansh Luchmun

Password Generator: Creates a password with two special characters, four numbers, 
and ten letters for 16 characters in total. The password is then shuffled in a 
different order and printed to the user.

"""

def main():
    special_chars = ['*','$','#','@','&','~','%']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    generate_pass(special_chars =special_chars, numbers=numbers, letters=letters)
    


#Function to handle password generator
def generate_pass(special_chars: list, numbers: list, letters: list):
    pass_list = []
    

    random_specials = random.choices(special_chars, k=2)
    random_numbers = random.choices(numbers, k=4)
    random_letters = random.choices(letters, k=10)
    pass_list.extend(random_specials)
    pass_list.extend(random_numbers)
    pass_list.extend(random_letters)
    shuffled_password = ""
    random.shuffle(pass_list)
    for x in pass_list:
        shuffled_password += x
    print(shuffled_password)

if __name__ == '__main__':
    main()