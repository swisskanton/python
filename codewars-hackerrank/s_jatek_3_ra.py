# Írjon ki egy 's'-t, ha, különben írja ki a számot
# A szám osztható 3-mal
# A szám osztható 3-mal, vagy osztható 5-tel
# A számben van 3 vagy osztható 3-mal

print('1. játék')
for i in range(1, 31):
    print(i if i % 3 else 's', end=' ')
print('\n----------')

print('2. játék')
for i in range(1, 31):
    print(i if i % 3 and i % 5 else 's', end=' ')
print('\n----------')

print('3. játék')
for i in range(1, 31):
    print('s' if '3' in str(i) or i % 3 == 0 else i, end=' ')