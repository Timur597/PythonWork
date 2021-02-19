t=-100
p=t
j=0
k=0
while t<=100:
	if(t%13==0)&(t%2==0):
	print(t,t**2)
	k+=1
	t+=1
print(k)

while p<=100:
	if p%2==1:	
		j+=1
		print(p)
		p += 7
print(j)