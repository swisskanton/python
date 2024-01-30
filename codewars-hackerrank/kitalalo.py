import random


fájl = open('szavak.txt', 'r', encoding='utf-8')
szavak = fájl.read().strip()[1:-1].split('", "')
fájl.close()
print(szavak)

rejtett = random.choice(szavak)
print(rejtett)

tipp = ''
tipp_szám = 1

while rejtett != tipp or tipp != 'stop':
    tipp = input('Kérem a tippet: ')
    if tipp == rejtett:
      print('Az eredmény:', tipp)
      break
    else:
        res = ''
        for i in range(6):
            res += tipp[i] if tipp[i] == rejtett[i] else '.'
        print(res)
    tipp_szám += 1

if tipp != 'stop':
   print(f'Az eredményt {tipp_szám} sikerült kitalálni.')
