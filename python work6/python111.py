'''suitcase9 = set()
i=0 
while i<5:
	i+=1
	s=input('give a five wear:',)
	suitcase9.add(s)
	list(set(suitcase9))
suitcase9.pop()
print(suitcase9)'''

'''Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: 
suitcase = [] 
Однако он
может вместить всего 5 вещей.
Положите 5 вещей в чемодан.
Вы передумали, и решили убрать последнюю вещь'''
suitcase1 = []
clothes = ['shirt','cap','t-shirt','boxes','glass']
g = 'glass'
suitcase1.extend (clothes)
print (suitcase1)
suitcase1.remove (g)
print (suitcase1)