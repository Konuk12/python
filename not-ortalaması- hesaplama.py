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
vize_yuzdesi = float(input('VİZE YÜZDESİNİ GİRİNİZ: '))
vize_notu = float(input('VİZE NOTUNUZ GİRİNİZ: '))

final_yuzdesi = float(input('FİNAL YÜZDESİ GİRİNİZ ='))
final_notu = float(input('FİNAL NOTUNUZU GİRİNİZ ='))

toplam_vize_notu = vize_notu * (vize_yuzdesi/100)
toplam_final_notu = final_notu * (final_yuzdesi/100)

ortalama = toplam_final_notu + toplam_vize_notu
print ('ORTALAMANIZ: ', ortalama)

if final_notu < 35:
 print('KALDINIZ!!!')
 
elif ortalama > 35:
 print('GEÇTİNİZ!!!')
 
else:
 print ('KALDINIZ!!!')