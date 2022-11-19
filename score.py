def main():
    score = float(input("Enter your score: "))
    print(determine_score(score))


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


main()
