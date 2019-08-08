def main():
    """
CP1404/CP5632 - Practical
Broken program to determine score status
"""
    result = "none"
    score = float(input("Enter score: "))
    result = generate_result(score)
    print(result)


def generate_result(score):
    if score < 0:
        result = "Invalid score"
    else:
        if score > 100:
            result = "Invalid score"
        elif score > 90:
            result = "Excellent"
        elif score > 50:
            result = "Passable"
        elif score < 50:
            result = "Bad"
    return result


main()


