#string işlemleri

str1 = 'ÖMER KONUK'
print(len(str1))

print(str1[0])
print(str1[9])
print(str1[-1])
print(str1[-10])

print(str1[::-1])

print(str1[2:0:-1])

print(str1[5:])
print(str1[:5])
print(str1[5:-4])

str1 = 'ÖMER KONUK'
str2 = str1[:4] + '-' + str1[5:]
print(str2)

print(str1.lower ())

print(str1.upper ())

print(str1.swapcase ())

print(str1.capitalize ())

