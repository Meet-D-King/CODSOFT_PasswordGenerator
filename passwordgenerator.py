import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    char_set = string.ascii_lowercase

    if use_uppercase:
        char_set += string.ascii_uppercase

    if use_digits:
        char_set += string.digits

    if use_special:
        char_set += string.punctuation

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password
    
def get_password_length():
    try:
        length = int(input("Enter length of password: "))
        if length > 0:
            return length
        else:
            print("Invalid input.")
            return get_password_length()
    except ValueError:
        print("Invalid input")
        return get_password_length()

def main():
    length = get_password_length()
        
    use_uppercase = input("Uppercase letters? (Y/N): ").upper() == 'Y'
    use_digits = input("Digits? (Y/N): ").upper() == 'Y'
    use_special = input("Special characters? (Y/N): ").upper() == 'Y'

    password = generate_password(length,use_uppercase,use_digits,use_special)
    print("\nGenerated Password: ", password)

main()
