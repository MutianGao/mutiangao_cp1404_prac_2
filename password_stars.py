MIN_LENGTH = 8


def main():
    enter_password = get_name()
    display_stars(enter_password)


def get_name():
    enter_password = input("Enter your password: ")
    while len(enter_password) < MIN_LENGTH:
        print(f"Invalid. Please enter at least {MIN_LENGTH} character")
        enter_password = input("Enter your password: ")
    return enter_password


def display_stars(enter_password):
    print(len(enter_password) * '*')


main()
