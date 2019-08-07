finish = False
while finish == False:

    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        fraction = numerator / denominator
        print(fraction)
        finish = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        print("User made '0' input. Cannot be divided by '0'!")
print("Finished.")

#When will a ValueError occur?
    #Answer: When the user makes an input other than integer to one or both of the input values, a ValueError will occur.

#When will a ZeroDivisionError occur?
    #Answer: When the user makes an input '0' to denominator value, the ZeroDivisionError Will occur.

#Could you change the code to avoid the possibility of a ZeroDivisionError?
    #Answer: Yes. i will create a boolean variable 'finish - false' and a while loop around error handaling code so that
    #it will keep asking the user till the integer or non-zero integer is entered,
