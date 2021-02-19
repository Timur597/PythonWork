'''str1={}
i=0
while i<10:
	i+=1
	num=input("vvedite 10 lybiux chisel:")
	set(str1).intersection(num)
	print(num)'''
	

z = set()
i = 0
while i < 10:
    i += 1
    x = input('введите 10 чисел: ',)
    z.add(x)
print(z)

for x in range (1,10):
    x = int(input('введите 10 чисел: '))
    z.add(x)
print(z)