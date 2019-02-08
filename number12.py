a=int(input())
N=a
rev=0
while (a>0):
 r=a%10
 rev=rev*10+r
 a=a//10
if(N==rev):
 print("yes")
else:
 print("no")
