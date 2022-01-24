print("""********************************************************
Hesap Makinesine Hoşgeldiniz!

Lütfen İşlem Seçiniz:

1. Toplama
2. Çıkarma
3. Bölme
4. Çarpma
5. Üs Alma
6. Karekök Alma
7. Logaritma
8. Dereceyi Radyana Çevirme
9. Sinüs
10. Kosinüs
11. Tanjant
12. Kotanjant
13. Çıkış
*******************************************************""")
import math
import time

while True:
    secim = input("İşlem seçiniz:")

    if (secim == "1"):
        x = int(input("İlk değeri giriniz:"))
        y = int(input("İkinci değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("{} + {} = {}".format(x,y,x+y))
    elif (secim == "2"):
        x = int(input("İlk değeri giriniz:"))
        y = int(input("İkinci değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("{} - {} = {}".format(x, y, x - y))
    elif (secim == "3"):
        x = int(input("İlk değeri giriniz:"))
        y = int(input("İkinci değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("{} / {} = {}".format(x, y, int(x / y)))
    elif (secim == "4"):
        x = int(input("İlk değeri giriniz:"))
        y = int(input("İkinci değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("{} * {} = {}".format(x, y, x * y))
    elif (secim == "5"):
        x = int(input("Tabanı giriniz:"))
        y = int(input("Üssü giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("{} üzeri {} = {}".format(x, y, x ** y))
    elif (secim == "6"):
        x = int(input("Değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("Karekök {} = {}".format(x,int(math.sqrt(x))))
    elif (secim == "7"):
        x = input("Değeri giriniz:")
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("log {} = {}".format(x,math.log(x)))
    elif (secim == "8"):
        x = int(input("Dereceyi giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("Radyan {} = {}".format(x,math.radians(x)))
    elif (secim == "9"):
        x = int(input("Değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("sin {} = {}".format(x,math.sin(x)))
    elif (secim == "10"):
        x = int(input("Değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print(math.cos(x))
    elif (secim == "11"):
        x = int(input("Değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("tan {} = {}".format(x,math.tan(x)))
    elif (secim == "12"):
        x = int(input("Değeri giriniz:"))
        işlem = print("İşlem yapılıyor..")
        time.sleep(2)
        print("cot {} = {}".format(x,math.cos(x)/math.sin(x)))
    elif (secim == "13"):
        break
    else:
        print("yanlış")
