x=int(input())
list=[]
for i in range(1,6):
	mul=x*i
	list.append(mul)
print(" ".join(map(str,list)))
