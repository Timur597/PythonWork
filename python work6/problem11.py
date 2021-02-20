menu = {'lagman': 120,
  	'plov': 120,
  	'borsh': 100}

menu['beshbarmak']=130
menu.update({'lagman':135})
menu.pop({'borsh'})
menu.update()
print(menu)