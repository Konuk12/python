#dizi ve liste işlemleri

dizi = [1 , 2 , 5 , 3]

print (dizi)

dizi2 = ['a' , 'grey' , 'red']

print (dizi2)

liste = ['veli', 5 ,'red', 8854]

print(liste)

print(liste [::-1])
print(liste [::-2])
print(liste [::2])
print(liste [:2])
print(liste [2:])

liste.append ('ÖMER')
print (liste)

liste.insert (3 , 'KONUK')
print(liste)

print(len(liste))

print(liste.count(5))

print(liste.count('ÖMER'))

Liste2 = ['MARMARA' , 'İSTANBUL' , 23, 'TÜRKİYE' , 2000 , 'DİYARBAKIR']
print (Liste2)

liste.extend (Liste2)
print (liste)

liste.reverse ()
print (liste)

liste.remove ('MARMARA')
print (liste)