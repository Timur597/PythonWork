'''
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
l = ["Razakov 32"]
try:
    l.append(set(values))
    print(l)
except SyntaxError: 
    print ("Ошибка")
except TypeError: 
    print('ошибка')
else:
    print("погнали дальше")
l = [10]
try:
    l.append(set(tables))
    print(l)
except NameError: 
    print ("Ошибка")
except IndentationError: 
    print('ошибка')
else:
    print("погнали дальше")
l = [1005]
try:
    l.append(set(tables))
    print(l)
except NameError: 
    print ("Ошибка")
except IndentationError: 
    print('ошибка')
else:
    print("погнали дальше")

l = ["tables"]
try:
    l.append(set(tables))
    print(l)
except NameError: 
    print ("Ошибка")
except IndentationError: 
    print('ошибка')
else:
    print("погнали дальше")
l = ["chairs"]
try:
    l.append(set(tables))
    print(l)
except NameError: 
    print ("Ошибка")
except IndentationError: 
    print('ошибка')
else:
    print("погнали дальше")
    
l = [23.00]
try:
    l.append(set(tables))
    print(l)
except NameError: 
    print ("Ошибка")
except IndentationError: 
    print('ошибка')
else:
    print("погнали дальше")'''
'''
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
l = []
try:
    l.append(set(values))
    print(l)
except SyntaxError: 
    print ("Ошибка")
except TypeError: 
    print('ошибка')
else:
    print("погнали дальше")'''

'''
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
test = open('database.txt', 'w')
test.write(str(values))
test.close()
l = []
pars = open('database.txt', 'r')
for r in pars:
    r = str(r)
    l.append(r)
pars.close()
a = list(values)
s = set(l)
if s:
    s.add(True)
    print(s)
print(all(values))'''

'''
o=[]
a=1
s=2
d=3
f=4
i=5

o.append(a)
o.append(s)
o.append(d)
o.append(f)
o.append(i)
print(min(o))'''



'''
s=input('input money for credit:')
b=60000
print(round(60000*3.47/100))
print('take your money babe')'''

'''values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
b=('disana')
l = []
try:
    l.append(set(values(b)))
    print(l)
except SyntaxError: 
    print ("Ошибка")
except TypeError: 
    print(',,,,')
except NameError:
    print(",,,,")'''

'''ERROR_CONDITIONS = IndexError,NameError,TypeError
try:
   ...
except ERROR_CONDITIONS as ae:
    print("Attribute Error while processing the configuration file!\n{0}\n".format( str(ae) ) )
    intReturnValue = 1'''

at = 10
ik = 15
wo = 20
try:
for e in range(-at, at):
except SyntaxError:
    print('hello')
except  IndentationError:  
    if at > '5':
        print("at" > 5)

        	
 