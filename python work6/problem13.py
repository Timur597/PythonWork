x =south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
  'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
x = set(south_american_countries)
dup = []
for c in x:
    if(south_american_countries.count(c) > 1):
        dup.append(c)
print(list(x))

set(dup)
print(dup)


# dup = []
# for c in x:
#     if(south_american_countries.count(c) > 1):
#         dup.append(c)


# frozenset(set(dup))
# print(list(dup))
# print(dup)
# dup = dict[set()]
# print(dup)