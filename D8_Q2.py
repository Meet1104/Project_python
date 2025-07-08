def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number to calculate the factorial for. Must be a non-negative integer.

    Returns:
    int: The factorial of the number n.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = 10
print(f"Factorial of {num} is:", factorial(num))

