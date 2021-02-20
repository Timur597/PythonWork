Вариант1
'''txt='Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
txt1=len(txt)
lower_case=txt.lower()
upper_case=txt.upper()
cut_len=txt1-(txt1//2)
printlen=lower_case[: cut_len]+upper_case[cut_len:]
print(printlen)'''
Вариант2
'''q = input('Введите текст : ')
w = input('Введите текст : ')
print(q.lower(), w.upper())'''
Вариант3
Tent1703, [20.02.21 10:08]
text = '''Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем a
SyntaxWarningsdg asd
gasdg
a
g adg
 adgadfgadf gafg adf
 g adfg adfg adfg dafg 
 afga'''

d = text.split()
r = len(d)

for g in range(r // 2):
    print(d[g].upper(), end='')
s = r - r // 2
while s < r:
    print(d[s].lower(), end='')
    s += 1