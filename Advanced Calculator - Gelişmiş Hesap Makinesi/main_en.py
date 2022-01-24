print("""********************************************************
Hesap Makinesine Hoşgeldiniz!

Lütfen İşlem Seçiniz:

1. Addition
2. Substraction
3. Division
4. Multiplication
5. Hyperpower
6. Extraction
7. Logarithm
8. Degrees to Radians
9. Sine
10. Cosine
11. Tangent
12. Cotaneget
13. Exit
*******************************************************""")
import math
import time

while True:
    choose = input("Choose your action:")
    process = "Processing is in progress..."
    if (choose == "1"):
        x = int(input("Enter the first value:"))
        y = int(input("Enter the second value:"))
        print(process)
        time.sleep(2)
        print("{} + {} = {}".format(x,y,x+y))
    elif (choose == "2"):
        x = int(input("Enter the first value:"))
        y = int(input("Enter the second value:"))
        print(process)
        time.sleep(2)
        print("{} - {} = {}".format(x, y, x - y))
    elif (choose == "3"):
        x = int(input("Enter the first value:"))
        y = int(input("Enter the second value:"))
        print(process)
        time.sleep(2)
        print("{} / {} = {}".format(x, y, int(x / y)))
    elif (choose == "4"):
        x = int(input("Enter the first value:"))
        y = int(input("Enter the second value:"))
        print(process)
        time.sleep(2)
        print("{} * {} = {}".format(x, y, x * y))
    elif (choose == "5"):
        x = int(input("Enter the base:"))
        y = int(input("Enter the second base:"))
        print(process)
        time.sleep(2)
        print("{} to the power of {} = {}".format(x, y, x ** y))
    elif (choose == "6"):
        x = int(input("Enter the value:"))
        print(process)
        time.sleep(2)
        print("Square root {} = {}".format(x,int(math.sqrt(x))))
    elif (choose == "7"):
        x = input("Enter the value:")
        print(process)
        time.sleep(2)
        print("log {} = {}".format(x,math.log(x)))
    elif (choose == "8"):
        x = int(input("Enter the value:"))
        print(process)
        time.sleep(2)
        print("Radian {} = {}".format(x,math.radians(x)))
    elif (choose == "9"):
        x = int(input("Enter the value:"))
        print(process)
        time.sleep(2)
        print("sin {} = {}".format(x,math.sin(x)))
    elif (choose == "10"):
        x = int(input("Enter the value:"))
        print(process)
        time.sleep(2)
        print(math.cos(x))
    elif (choose == "11"):
        x = int(input("Enter the value:"))
        print(process)
        time.sleep(2)
        print("tan {} = {}".format(x,math.tan(x)))
    elif (choose == "12"):
        x = int(input("Enter the value:"))
        print(process)
        time.sleep(2)
        print("cot {} = {}".format(x,math.cos(x)/math.sin(x)))
    elif (choose == "13"):
        break
    else:
        print("false")
