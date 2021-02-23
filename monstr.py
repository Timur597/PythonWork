'''r = open('/home/azat/Рабочий стол/users.txt', 'w')
name = input("login: ")
lastname = input("password: ")
r.write(f"Hi {name} {lastname}")
r.close

with open('users.txt', 'r') as file:
    print(file.read())'''
 '''z=open('/home/azat/Рабочий стол/users.txt', 'w')
 login = input ('Your login: ')
 password = input ('Your password: ')
 z.write(f'hello man write your{login} ? And your password is {password} ?')
 z.close()
 with open ('users.txt','r') as file:
     print (file.read())'''

d=open('/home/azat/Рабочий стол/users.txt', 'w')
r.write("Python is a widely used high-level programming language for general-purpose"
"programming, created by Guido van Rossum and first released in 1991. An interpreted"
"language, Python has a design philosophy that emphasizes code readability notably"
"using whitespace indentation to delimit code blocks rather than curly brackets or"
"keywords, and a syntax that allows programmers to express concepts in fewer lines of"
"code than might be used in languages such as C++ or Java")

with open ('direct.txt','r') as file:
	print(file.read())

