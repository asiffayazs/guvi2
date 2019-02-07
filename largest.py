a=float(input("enter number"))
b=float(input("enter number"))
c=float(input("enter number"))

if a>b and a>c:
  largest=a
elif b>a and b>c:
  largest=b
else:
  largest=c
print("the largest number is",largest)
