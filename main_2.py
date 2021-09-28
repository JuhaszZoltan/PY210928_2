import random

print(random.randint(100, 999))
print(random.randint(0, 25))

szam = random.randint(0, 24) + random.random()
print(szam)

szam = random.randint(0, 250) / 10
print(szam)

szam = random.randint(1, 49) * 2
print(szam)

szam = random.randint(20, 40) * 5
print(szam)

szam = random.randint(0, 1000000)
# if szam == 1000000: print('7 hegyű')
# if szam < 1000000 and szam >= 100000: print('6 jegyű')
# if szam < 100000 and szam >= 10000: print('5 jegyű')
# if szam < 10000 and szam >= 1000: print('4 jegyű')
# if szam < 1000 and szam >= 100: print('3 jegyű')
# if szam < 100 and szam >= 10: print('2 jegyű')
# if szam < 10 and szam >= 1: print('1 jegyű')

if    szam == 1000000: print('7 hegyű')
elif  szam >= 100000:  print('6 jegyű')
elif  szam >= 10000:   print('5 jegyű')
elif  szam >= 1000:    print('4 jegyű')
elif  szam >= 100:     print('3 jegyű')
elif  szam >= 10:      print('2 jegyű')
else:                  print('1 jegyű')

print(f'1:[{random.randint(1, 6)}] 2:[{random.randint(1, 6)}] 3:[{random.randint(1, 6)}] 4:[{random.randint(1, 6)}] 5:[{random.randint(1, 6)}] 6:[{random.randint(1, 6)}]')

