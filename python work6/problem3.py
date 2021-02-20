'''farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm3=(set(farm_2).difference(farm_1))
print(farm3)'''
farm_1 = {"dog", "cat", "mouse", "sheep"} 
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(len(farm_1), len(farm_2), farm_2-farm_1)

'''farm_1 = {"dog", "cat", "mouse", "sheep"} 
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm3=farm2.difference(farm1)
print(farm3)'''