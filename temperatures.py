MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = C_to_F(celsius)
            print(f"Result: {fahrenheit:} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = F_to_C(fahrenheit)
            print(f"Result: {celsius:} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def C_to_F(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def F_to_C(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
