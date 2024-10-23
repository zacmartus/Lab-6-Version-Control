def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(input_string):
    encoded_string = ''
    for char in input_string:
        if char.isdigit():
            new_digit = (int(char) + 3) % 10
            encoded_string += str(new_digit)

        else:
            encoded_string += char

    return encoded_string

def decode(encoded_pass):
    pass


def main():
    encoded_string = ''
    while True:
        menu()
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            user_password = input('Please enter your password to encode: ')
            encoded_string = encode(user_password)
            print('Your password has been encoded and stored!')

        elif user_input == 2:
            pass

        elif user_input == 3:
            break














if __name__ == "__main__":
    main()
