#!/usr/bin/env python3

# Inside sequences.py in the lib folder

def print_fibonacci(length):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    print(fibonacci_sequence)

# Test your function with print_fibonacci(9)
print_fibonacci(9)
