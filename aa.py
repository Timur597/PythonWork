#a=open('/home/azat/Рабочий стол/python.txt', 'w')
#r.write('''Python is a widely used high-level programming language for general-purpose
#programming, created by Guido van Rossum and first released in 1991. An interpreted
#language, Python has a design philosophy that emphasizes code readability (notably
#using whitespace indentation to delimit code blocks rather than curly brackets or
#keywords), and a syntax that allows programmers to express concepts in fewer lines of
#code than might be used in languages such as C++ or Java''')
#r.close()
#with open('direct.txt','r') as file:
#	print(file.read())

'''s = open ('задание3.txt', 'w')
s.write ("What's a wonderfull day!")
s.close()
c = "What's a wonderfull day!"
with open ('задание3.txt','r') as file:
    print (file.read())
    if c[9] == 'w':
        print ('Да, в тексте есть "W"')
    else:
        print ('Нет, в тексте нет "w"')'''
        
'''s=open('/home/azat/Рабочий стол/python.txt','r')
if "w" in s.read():
    print("yes")
else:
   	print('no')'''

'''h = open('/home/azat/Рабочий стол/python.txt', 'r')
t_words = []
c = (h.read().split())
for x in c:
    if "t" in x:
        t_words.append(x)
    if "T" in x:
        t_words.append(x)
print(t_words)
h.close()'''
'''h = open('/home/azat/Рабочий стол/python.txt', 'r')
full.txt=f.read()
a=input('login :')
s=input('password :')
if a and s in full.txt:
	print('True')
else:
	print('Error')'''
'''
file = open('/home/azat/Рабочий стол/python.txt', 'r')
file.write(input('Введите логин: ') + ' ' + input('Введите пароль: ')+'\n')
file.close()'''





'''with open('database.txt', 'r') as f:
    full_txt = f.read()
    enLog = input('Login: ')
    enPass = input('Password: ')
    if enLog and enPass in full_txt:
        print('True')
    else:
        print('Not true')'''

'''t = open ("database.txt", "w")
t.write("login : kamikadze ,password : lololo, Login: jojopa, password: hohoho")
t.close()
m = 'kamikadze'
b = 'jojopa'
z = input ("Can you please registrate in our socialsite? + or - ")
if z == "+":
    print('Thank you! ')
else:
    print ("Ok!Fuck you!")
    print('Shutdown this programm,old bitch! ')
    print(input("!push Ctrl z! "))
i = input('Your login: ')
if i == m :
    print(f"Your login {i} is busy. ")
    print('Please registrate new login \n==>==>==>==>==>==>==>')
    i = (input('Your new login: '))
if i == b:
    print(f"Your login {i} is busy. ")
    print('Please registrate new login \n==>==>==>==>==>==>==>')
    i= input('Your new login: ')
if i != m or i != b:
    p = input(f"If this log {i} yours,please write one more time: ")
    print("Good!Next step :ъ ")
    c = input('Your password: ')
    x = input ('Try again please :')
if c == x:
    print(f'Your login {p} and password {x} are correct!')
    u = open ('database.txt','w')
    u.write(f"login : {i} and password : {x}")
    u.close()
else:
    print(f'Your login {i} and password {x} are incorrect!')

u1 = open ("database.txt", "r")
print(u1.read())
u1.close()'''

'''f=open('database.txt', 'r')
x=(f.read().split())
n=input("input login:")
for i in range(int(len(x))):
    if x[i]==n:
        print('login is busy')
        log=input('input new Login:')
        pas=input('input new password:')
        pas2=input('repeat new password again:')
        if pas==pas2:
            print('registrate new users')
            l=open('database.txt', 'a')
            l.write(f"login: {log}, password:{pas}\n")
            l.close()
            break'''

print('''Войти или зарегистрироваться
    yes      no ''')
q = input(':   ')
w = input(':   ')
if 'yes' in q:
    print ('Введите пароль и логин')
if 'no' in w:
    print('Всего доброго')

a = input("логин: ")
b = input("пароль: ")

r = open('/home/azat/Рабочий стол/datebase.txt', 'r')
for x in r:
    if 'qwerty' in x:
        print('такой логин уже существует.')
    else: 
        print('Зарегистрируйтесь еще раз')    


r.close()

r = open('/home/azat/Рабочий стол/datebase.txt', 'a')
a = input("логин: ")
b = input("пароль: ")
c = input("потвердите пароль: ")
if b == c:
    print('Реситрация прошло успешно')
else:
    print('введите пароль еще раз')
    b = input("пароль: ")
    c = input("потвердите пароль: ")
    print('Реситрация прошло успешно')

r.write(f"name: {a}, password: {b}")
r.close() 