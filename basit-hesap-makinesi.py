A = float(input('A SAYISINI GİRİNİZ: '))
B = float(input('B SAYISINI GİRİNİZ: '))

print('a = toplama')
print('b = çıkarma')
print('c = çarpma')
print('d = bölme')
print('e = kuvvet alma')

islem = input('YAPACAĞINIZ İŞLEMİ SEÇİN: ')

if islem == 'a':
    sonuc = A + B
    print('sonuc = A + B =', sonuc)
elif islem == 'b':
    sonuc = A - B
    print('sonuc = A - B =', sonuc)
elif islem == 'c':
    sonuc = A * B
    print('sonuc = A * B =', sonuc)
elif islem == 'd':
    if B != 0:  # Check for division by zero
        sonuc = A / B
        print('sonuc = A / B =', sonuc)
    else:
        print('Bölme işlemi için B sıfır olamaz.')
elif islem == 'e':
    sonuc = A ** B
    print('sonuc = A ** B =', sonuc)
else:
    print('Geçersiz işlem seçimi. Lütfen doğru bir işlem seçin.')