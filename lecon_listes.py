liste = [4, 1.1, 8, 'a', True]

print(liste[4])

print(len(liste))

liste2 = liste[:]

print(liste2)

liste2 = liste[4:]

print(liste2)

print(liste[-2])

print(liste[1:])

print(liste[::-1]) # slicing

liste[3] = 25
print (liste)

del liste[3]
print (liste)

liste.append(50)
print (liste)


for x in liste:
    print(x * x)

liste3 = [x**2 for x in liste] # list comprehension
print(liste)
print(liste3)

liste4 = range(1,11)
print(liste4)
for x in liste4:
    print(x)

if 30 in liste:
    print('found')
else:
    print('not found')


print([x**2 for x in range(1,11,2)])