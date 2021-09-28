import random as rnd

a = rnd.randint(10, 50)
b = rnd.randint(10, 50)

valasz = int(input(f'{a} + {b} = '))

if a + b == valasz: print('ugy van')
else: print(f'nem, hanem {a + b}')