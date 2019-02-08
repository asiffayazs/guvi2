r = int(input())
if r > 1:
   for i in range(2,r):
       if (r % i) == 0:
           print("no")
           break
   else:
       print("yes")    
else:
   print("Invalid")
