a=int(input())
b=int(input())
c=[]
d=0
for i in range(a):
	x=int(input())
	c.insert(i,x)
for j in range(b):
	d=d+c[j]
print(d)
	
