# Define limit
limit = int(input())

# Initialize first two Fibonacci numbers
fib1 = 0
fib2 = 1

list_numbers = []

# Generate and print the rest of the Fibonacci sequence up to the limit
while fib2 <= limit:
    fib = fib1 + fib2

    print(fib)
    fib1 = fib2
    fib2 = fib
