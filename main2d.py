from figure2d import *
import os
menu=int
while(menu!=0):
    menu2=0
    os.system('cls')
    print("=======================")
    print("1. Segitiga")
    print("2. Segiempat")
    print("")
    print("")
    print("0. Exit")
    print("=======================")
    menu=int(input())
    if(menu==1):
        os.system('cls')
        print("=======================")
        print("Segitiga")
        print("1. Sama Kaki")
        print("2. Sama Sisi")
        print("=======================")
        menu2=int(input())
        os.system('cls')
        print("=======================")
        if(menu2==1):
            alas=int(input("Masukkan alas : "))
            tinggi=int(input("Masukkan tinggi : "))
            a=Samakaki(alas, tinggi)
        elif(menu2==2):
            sisi=int(input("Masukkan sisi : "))
            tinggi=int(input("Masukkan tinggi : "))
            a=Samasisi(sisi, tinggi)
    elif(menu==2):
        os.system('cls')
        print("=======================")
        print("1. Persegi")
        print("2. Trapesium")
        print("3. Jajargenjang")
        print("=======================")
        menu2=int(input())
        os.system('cls')
        print("=======================")
        if(menu2==1):
            panjang=int(input("Masukkan panjang : "))
            lebar=int(input("Masukkan lebar : "))
            a=Persegi(panjang,lebar)
            os.system('cls')
            print("Persegi")
        elif(menu2==2):
            alas=int(input("Masukkan alas : "))
            tutup=int(input("Masukkan tutup : "))
            tinggi=int(input("Masukkan tinggi : "))
            a=Trapesium(alas, tutup, tinggi)
            os.system('cls')
            print("Trapesium")
        elif(menu2==3):
            alas=int(input("Masukkan alas : "))
            tinggi=int(input("Masukkan tinggi : "))
            a=Jajargenjang(alas, tinggi)
            os.system('cls')
            print("Jajargenjang")
    if (menu2 >= 1 and menu2 <= 3):
        print("=======================")
        print("Luas = " + str(a.hitung_luas()))
        print("Keliling = " + str(a.hitung_keliling()))
        print("=======================")
        try:
            input("Tekan Enter untuk melanjutkan...")
        except SyntaxError:
            pass