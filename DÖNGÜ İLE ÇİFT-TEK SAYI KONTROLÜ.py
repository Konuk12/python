while True:
    sayi = input('BİR SAYI GİRİNİZ veya "DUR" yazarak çıkış yapın: ')

    if sayi.upper() == 'DUR':
        print('Çıkış yapılıyor...')
        break

    sayi = int(sayi)  # Convert input to an integer

    if sayi % 2 == 1:
        print('SEÇTİĞİNİZ SAYI TEK SAYIDIR')
    
    elif sayi % 2 == 0:
        print('SEÇTİĞİNİZ SAYI ÇİFT SAYIDIR')
