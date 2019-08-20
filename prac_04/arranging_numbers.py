def main():

    numbers = []

    for i in range(0, 5):
        numbers.append(int(input("Enter a number: ")))
    first_number = numbers[0]
    last_number = numbers[4]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers)/len(numbers)

    print("The first number is {}".format(first_number))
    print("The last number is {}".format(last_number))
    print("The smallest number is {}".format(smallest_number))
    print("The largest number is {}".format(largest_number))
    print("The average number is {}".format(average_number))


main()
