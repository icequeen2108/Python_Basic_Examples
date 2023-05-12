x = float(input())
y = float(input())

temporary_var = x
x = y
y = temporary_var

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))