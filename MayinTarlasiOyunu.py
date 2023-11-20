"""  Öğrenci No: 22100011074
     Ad-Soyad: Sude Özsoy    """

import random
toppuan = 0                                   # oynanan tüm oyunların puanlarının toplamını gösterir.
while True:
    print("Mayın Tarlası Oyunu")
    print(f"1. Basla                  Toplam Puanınız:{toppuan}\n"                 
          "2. Sonlandır ")
    secim = int(input(">>"))
    if secim == 1:
        print("1. Gizli mod\n"
              "2. Açık mod")
        secim = int(input(">>"))
        puan = 0
        if secim == 1:
            while True:
                matrix = int(input('Oyun alanı için boyut bilgisi giriniz(min-10x10): '))
                if matrix < 10:
                    print("Yalnızca 10 ve 10'dan büyük sayı girmelisiniz.")
                    continue
                else:                      # 10dan büyük şartı sağlanıyorsa sonsuz döngüden çıkacak.
                    break
            liste = []
            gizli_list = []
            for i in range(matrix):
                liste.append(['?'] * matrix)         # tamamının soru işareti olduğu liste.
            for i in range(matrix):
                gizli_list.append(['.'] * matrix)    # Mayınların yerleşeceği liste, öncesinde tamamına . koydum.
            mayin_say = int(matrix ** 2 * 0.3)    # kullanıcının gireceği alan sayısına göre olması gerekn mayın sayısı.

            for i in range(mayin_say):
                while True:
                    x = random.randint(0, matrix-1)   # rastgele bir x ve y sayısı oluşturur koordinat için.
                    y = random.randint(0, matrix-1)
                    if gizli_list[x][y] == 'X':       # eğer daha önce mayın koyulmuşsa tekrar koordinat alması için.
                        continue
                    else:
                        gizli_list[x][y] = 'X'        # ratgele alınan koordinatlara Xi yani mayını koyar.
                        break
            for i in range(0, matrix):
               print('  '.join(liste[i]))             # tabloyu tek satırda yazdırmak için join kullandım.

            while True:
                x = int(input("\nYatayı giriniz(0-{} arası): ".format(matrix-1)))
                y = int(input("Düşeyi giriniz(0-{} arası): ".format(matrix-1)))
                if 0 <= x <= matrix-1 or 0 <= y <= matrix-1:  # koordinatların dışında sayı girilmemesi için şart.
                    mayin = 0                                 # her yeni koordinatın çevresine bakarkn mayın 0dan başlar
                    if liste[x][y] != '?' and gizli_list[x][y] != 'X':   # ? yerinde rakam varsa oraya bakılmış demektir.
                        print('Bu noktaya bakıldı. Başka sayi girin.')
                        continue
                    if gizli_list[x][y] == 'X':               # eğer mayını seçtiyse kaybetmiş olur.
                        print('\n--KAYBETTİNİZ--')
                        for i in range(0, matrix):
                            print('  '.join(gizli_list[i]))   # tablonun son halini yazdırır.
                        print(f"\nOyundan alınan puan:{puan}\n")
                        break
                    else:
                        if x == 0 and y == 0:                  # girilen koordinat sol üst köşeyse
                            if gizli_list[x][y+1] == 'X':      # 3 kenarında mayın olup olmadığını kontrol eder.
                                mayin += 1                     # mayın varsa mayın sayısını artırır.
                            if gizli_list[x+1][y] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y+1] == 'X':
                                mayin += 1
                        elif x == 0 and y == (matrix-1):         # sağ üst köşeyse
                            if gizli_list[x+1][y] == 'X':
                                mayin += 1
                            if gizli_list[x][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y-1] == 'X':
                                mayin += 1
                        elif x == matrix-1 and y == 0:           # sol alt köşeyse
                            if gizli_list[x - 1][y] == 'X':
                                mayin += 1
                            if gizli_list[x][y + 1] == 'X':
                                mayin += 1
                            if gizli_list[x - 1][y + 1] == 'X':
                                mayin += 1
                        elif x == matrix-1 and y == matrix-1:      # sağ alt köşeyse
                            if gizli_list[x - 1][y] == 'X':
                                mayin += 1
                            if gizli_list[x][y - 1] == 'X':
                                mayin += 1
                            if gizli_list[x - 1][y - 1] == 'X':
                                mayin += 1
                        elif 0 < x < (matrix-1) and y == 0:       # sol kenarsa
                            if gizli_list[x-1][y] == 'X':       # 5 kenarında mayın olup olmadığını kontrol eder.
                                mayin += 1
                            if gizli_list[x-1][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y] == 'X':
                                mayin += 1
                        elif x == 0 and 0 < y < (matrix-1):      # üst kenarsa
                            if gizli_list[x][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x][y+1] == 'X':
                                mayin += 1
                        elif 0 < x < (matrix-1) and y == (matrix-1):   # sağ kenarsa
                            if gizli_list[x-1][y] == 'X':
                                mayin += 1
                            if gizli_list[x-1][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y] == 'X':
                                mayin += 1
                        elif x == (matrix-1) and 0 < y < (matrix-1):  # alt kenarsa
                            if gizli_list[x][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x-1][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x-1][y] == 'X':
                                mayin += 1
                            if gizli_list[x-1][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x][y+1] == 'X':
                                mayin += 1
                        elif 0 < y < (matrix-1) and 0 < x < (matrix-1):  # orta kısımsa
                            if gizli_list[x-1][y-1] == 'X':            # 8 kenarında mayın olup olmadığını kontrol eder.
                                mayin += 1
                            if gizli_list[x][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y-1] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y] == 'X':
                                mayin += 1
                            if gizli_list[x+1][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x-1][y+1] == 'X':
                                mayin += 1
                            if gizli_list[x-1][y] == 'X':
                                mayin += 1
                        puan += 1
                        toppuan += 1
                        print(f'Güncel puanınız:{puan}')
                        liste[x][y] = str(mayin)                   # açılan kısıma kenarında kaç mayın varsa yazdırır.
                        gizli_list[x][y] = str(mayin)
                        for i in range(0, matrix):                 # tablonun son halini ekrana yazdırır.
                            print('  '.join(liste[i]))
                else:                                           # matrix alanı dışında bir sayı girerse
                    print(f'Yanlış sayı girişi. 0-{matrix-1} aralığında bir sayi girin.')
                    continue

                devam = False
                for i in range(matrix):
                    for j in range(matrix):
                        if liste[i][j] == '?':     # eğer hala açılmamış kısım varsa devam değişkeninin true yapacak.
                            devam = True

                if devam == False:                # eğer durum değişkeni true olmadıysa tüm tabloya bakılmış demktir.
                    print(f'Hiç mayına basmadınız.Oyun bitti.KAZANDINIZ.\nPuan durumunuz:{puan}')
                    break
        elif secim == 2:                          # açık mod
            while True:
                matrix = int(input('Oyun alanı için boyut bilgisi giriniz(min-10x10): '))
                if matrix < 10:
                    print("Yalnızca 10 ve 10'dan büyük sayı girmelisiniz.")
                    continue
                else:                            # 10dan büyük şartı sağlanıyorsa döngüden çıkacak.
                    break
            liste = []
            for i in range(matrix):              # Mayınların yerleşeceği liste, öncesinde tamamına ? koydum.
                liste.append(['?'] * matrix)

            mayin_say = int(matrix**2*0.3)       # kullanıcının gireceği alan sayısına göre olması gerekn mayın sayısı.

            for i in range(mayin_say):
                while True:
                    x = random.randint(0, matrix-1)     # rastgele bir x ve y sayısı oluşturur koordinat için.
                    y = random.randint(0, matrix-1)
                    if liste[x][y] == 'X':              # eğer daha önce mayın koyulmuşsa tekrar koordinat alması için.
                        continue
                    else:
                        liste[x][y] = 'X'               # ratgele alınan koordinatlara Xi yani mayını koyar.
                        break

            for i in range(0, matrix):                  # tabloyu ekrana yazdırır.
               print('  '.join(liste[i]))

            while True:
                x = int(input("\nSatırı giriniz(0-{} arası): ".format(matrix-1)))
                y = int(input("Sütunu giriniz(0-{} arası): ".format(matrix-1)))
                if 0 <= x <= matrix-1 or 0 <= y <= matrix-1:      # koordinatların dışında sayı girilmemesi için şart.
                    mayin = 0                                 # her yeni koordinatın çevresine bakarkn mayın 0dan başlar
                    if liste[x][y] != '?' and liste[x][y] != 'X':                    # ? yerinde rakam varsa oraya bakılmış demektir.
                        print('Bu noktaya bakıldı. Başka sayi girin.')
                        continue
                    if liste[x][y] == 'X':                    # eğer mayını seçtiyse kaybetmiş olur.
                        print(f"\n--KAYBETTİNİZ--\nOyundan alınan puan:{puan}\n")
                        break
                    else:
                        if x == 0 and y == 0:                 # girilen koordinat sol üst köşeyse
                            if liste[x][y+1] == 'X':          # 3 kenarında mayın olup olmadığını kontrol eder.
                                mayin += 1                    # mayın varsa mayın sayısını artırır.
                            if liste[x+1][y] == 'X':
                                mayin += 1
                            if liste[x+1][y+1] == 'X':
                                mayin += 1
                        elif x == 0 and y == (matrix-1):        # sağ üst köşeyse
                            if liste[x+1][y] == 'X':
                                mayin += 1
                            if liste[x][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y-1] == 'X':
                                mayin += 1
                        elif x == matrix-1 and y == 0:          # sol alt köşeyse
                            if liste[x - 1][y] == 'X':
                                mayin += 1
                            if liste[x][y + 1] == 'X':
                                mayin += 1
                            if liste[x - 1][y + 1] == 'X':
                                mayin += 1
                        elif x == matrix-1 and y == matrix-1:   # sağ alt köşeyse
                            if liste[x - 1][y] == 'X':
                                mayin += 1
                            if liste[x][y - 1] == 'X':
                                mayin += 1
                            if liste[x - 1][y - 1] == 'X':
                                mayin += 1
                        elif 0 < x < (matrix-1) and y == 0:     # sol kenarsa
                            if liste[x-1][y] == 'X':          # 5 kenarında mayın olup olmadığını kontrol eder.
                                mayin += 1
                            if liste[x-1][y+1] == 'X':
                                mayin += 1
                            if liste[x][y+1] == 'X':
                                mayin += 1
                            if liste[x+1][y+1] == 'X':
                                mayin += 1
                            if liste[x+1][y] == 'X':
                                mayin += 1
                        elif x == 0 and 0 < y < (matrix-1):     # üst kenarsa
                            if liste[x][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y] == 'X':
                                mayin += 1
                            if liste[x+1][y+1] == 'X':
                                mayin += 1
                            if liste[x][y+1] == 'X':
                                mayin += 1
                        elif 0 < x < (matrix-1) and y == (matrix-1):    # sağ kenarsa
                            if liste[x-1][y] == 'X':
                                mayin += 1
                            if liste[x-1][y-1] == 'X':
                                mayin += 1
                            if liste[x][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y] == 'X':
                                mayin += 1
                        elif x == (matrix-1) and 0 < y < (matrix-1):   # alt kenarsa
                            if liste[x][y-1] == 'X':
                                mayin += 1
                            if liste[x-1][y-1] == 'X':
                                mayin += 1
                            if liste[x-1][y] == 'X':
                                mayin += 1
                            if liste[x-1][y+1] == 'X':
                                mayin += 1
                            if liste[x][y+1] == 'X':
                                mayin += 1
                        elif 0 < y < (matrix-1) and 0 < x < (matrix-1):     # orta kısımsa
                            if liste[x-1][y-1] == 'X':                 # 8 kenarında mayın olup olmadığını kontrol eder.
                                mayin += 1
                            if liste[x][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y-1] == 'X':
                                mayin += 1
                            if liste[x+1][y] == 'X':
                                mayin += 1
                            if liste[x+1][y+1] == 'X':
                                mayin += 1
                            if liste[x][y+1] == 'X':
                                mayin += 1
                            if liste[x-1][y+1] == 'X':
                                mayin += 1
                            if liste[x-1][y] == 'X':
                                mayin += 1
                        puan += 1
                        toppuan += 1
                        print(f'Güncel puanınız:{puan}')
                        liste[x][y] = str(mayin)                 # açılan kısıma kenarında kaç mayın varsa yazdırır.
                        for i in range(0, matrix):               # tablonun son halini yazdırır.
                            print('  '.join(liste[i]))
                else:                                            # matrix alanı dışında bir sayı girerse
                    print(f'Yanlış sayı girişi. 0-{matrix-1} aralığında bir sayi girin.')
                    continue

                devam = False
                for i in range(matrix):
                    for j in range(matrix):
                        if liste[i][j] == '?':
                            devam = True             # eğer hala açılmamış kısım varsa devam değişkeninin true yapacak.

                if devam == False:                  # eğer durum değişkeni true olmadıysa tüm tabloya bakılmış demktir.
                    print(f'Hiç mayına basmadınız.Oyun bitti.KAZANDINIZ.\nPuan durumunuz:{puan}')
                    break
        else:                                     # menü ekranında yanlış secim yapılırsa baştaki menüye döndürür.
            print('Yanlış sayi girişi. Lütfen doğru seçim yapın.\n')
            continue
    elif secim == 2:
        break
    else:
        print('Yanlış sayi girişi. Lütfen doğru seçim yapın.\n')
        continue
