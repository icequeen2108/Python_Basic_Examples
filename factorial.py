#solution 1
# number = int(input())
# factorial = 1
# if number < 0:
#     print("Factorial doesn't exist.")
# elif number == 0:
#     print("Factorial of 0 is 1.")
# else:
#     for i in range(1, number+1):
#         factorial = i * factorial
#     print("The factorial of", number, "is", factorial)

# solution 2 - recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x -1))
    
number = int(input())
result = factorial(number)
print(result)