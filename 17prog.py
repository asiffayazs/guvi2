y=int(input())
a=list(map(int,str(y)))
b=list(map(lambda x:x**3,a))
if(sum(b)==y):
    print("yes")
else:
    print("no")
