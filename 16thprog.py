a,b=input().split()
a=int(a)
b=int(b)
list=[]
for num in range(a+1,b):
	for d in range(2,num):
		if num%d==0:
			break
	else:
		list.append(num)
print(" ".join(map(str,list)))
