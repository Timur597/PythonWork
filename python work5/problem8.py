'''tuple1 = (1, 2, 3, 4, 8, 12, 3, 34, 
             67, 45, 1, 1, 43, 65, 9) 
  
print(tuple1[0:3])
print(tuple1[3:6])
print(tuple1[6:9])
print(tuple1[9:12])
print(tuple1[12:15])'''

tuple1= (1, 2, 3, 4, 8, 12, 3, 34, 
             67, 45, 1, 1, 43, 65, 9)
for x in range(0, len(tuple1), 3):
	print(tuple1[x:x+3])