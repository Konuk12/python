def DİKDÖRTGEN():
    print('ALAN = A*B')
    A = int(input('A KENARINI GİRİNİZ: '))
    B = int(input('B KENARINI GİRİNİZ: '))
    ALAN = A * B
    print('ALAN = ', ALAN)

def KARE():
    print('ALAN = A^2')
    A = int(input('A KENARINI GİRİNİZ:'))
    ALAN = A ** 2
    print('ALAN = ', ALAN)

print('KARE Mİ DİKDÖRTGEN Mİ?')
secim = input('HANGİSİNİN ALANINI HESAPLAMAK İSTİYORSUN = ')

if secim.upper() == 'KARE':
    KARE()
elif secim.upper() == 'DİKDÖRTGEN':
    DİKDÖRTGEN()
else:
    print('YANLIŞ SEÇİM YAPTINIZ!!!')