MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    score = float(input("Please enter your score: "))
    get_valid_score(score)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Please enter your score: "))
            get_valid_score(score)
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            score_stars(score)
        else:
            print("Invalid.")
        print(MENU)
        choice = input(">>>").upper()
    print("Good bye.")


def get_valid_score(score):
    while 0 < score < 100:
        print(f"enter score: {score}")
        return score
    else:
        print("Invalid.")


def determine_score(score):
    if 0 < score < 50:
        score_level = "bad"

    elif score < 90:
        score_level = "pass"

    elif score < 100:
        score_level = "excellent"

    else:
        score_level = "Invalid"

    return score_level


def score_stars(score):
    print(int(score) * '*')


main()
