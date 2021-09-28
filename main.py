a = True
b = False

if a and b: print('1: igaz')
else: print('1: hamis')

if not b: print('2: igaz')
else: print('2: hamis')

if a or b: print('3: igaz')
else: print('3: hamis')

if a != b: print('4: igaz')
else: print('4: hamis')

if a == b: print('5: igaz')
else: print('5: hamis')

if a or b and a == a: print('6: igaz')
else: print('6: hamis')


if "krumpli" == "burgonya": print('7: igaz')
else: print('7: hamis')

if 10 > 20: print('8: igaz')
else: print('8: hamis')

if 20 > 33 and 102 < 1024: print('9: igaz')
else: print('9: hamis')


# if [ide bármilyen feltétel kerül]:
#     [ez akkor fut le, ha a fenti feltétel igaz]
# else: [ez pedig akkor futr le, ha a fenti hamis]