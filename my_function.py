def sum_numbers(a, b):
    """
    Function to calculate the sum of two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum of", num1, "and", num2, "is:", sum_numbers(num1, num2))

if __name__ == "__main__":
    main()
