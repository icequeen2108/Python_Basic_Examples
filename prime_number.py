lower = int(input())
upper = int(input())
print("Prime numbers between", lower, "and", upper, "are:")
list_prime = []
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list_prime.append(num)

print(list_prime)
print(' '.join(map(str, list_prime)))