# Higher-Order Lambda Functions

This Python project demonstrates the use of higher-order functions with lambda expressions. The project defines a function `apply_operation` that applies a given operation (defined as a lambda function) to each element in a list of numbers.

## Overview

In this project, the focus is on:
- Understanding higher-order functions in Python.
- Using lambda functions to define operations.
- Applying those operations to a list of numbers and returning the results.

## Function Details

The main function is:

```python
def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.
    
    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]
```
##  Requirements
Python 3.12.5
