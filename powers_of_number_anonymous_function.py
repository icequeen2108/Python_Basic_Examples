terms = int(input())
number = int(input())

result = list(map(lambda x: number ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print(f"{number} raised to power",i,"is",result[i])