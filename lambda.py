def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.
    
    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]

# Example Usage:

numbers = [1, 2, 3, 4, 5]

# Doubling the numbers
doubled = apply_operation(numbers, lambda x: x * 2)
print("Doubled:", doubled)  # Output: [2, 4, 6, 8, 10]

# Squaring the numbers
squared = apply_operation(numbers, lambda x: x ** 2)
print("Squared:", squared)  # Output: [1, 4, 9, 16, 25]

# Filtering odd numbers
filtered = apply_operation(numbers, lambda x: x if x % 2 != 0 else None)
filtered = [num for num in filtered if num is not None]  # Remove None values
print("Filtered (odd numbers):", filtered)  # Output: [1, 3, 5]
