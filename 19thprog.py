a=int(input())
factorial = 1
if a < 0:
   print("Factorrial does not exist for negative numbers")
elif a == 0:
   print("1")
else:
   for i in range(1,a + 1):
       factorial = factorial*i
   print(factorial)
