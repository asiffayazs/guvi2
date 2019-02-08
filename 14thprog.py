g=input().split()
n=int(g[0])
q=int(g[1])
list=[]
for i in range(n+1,q):
    if(i%2!=0):
    	list.append(i)
print(" ".join(map(str,list)))
