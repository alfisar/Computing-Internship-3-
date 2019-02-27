from figure3d import *
import os
menu=int
while(menu!=0):
    os.system('cls')
    print("=======================")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("")
    print("")
    print("0. Exit")
    print("=======================")
    menu=int(input())
    os.system('cls')
    print("=======================")
    if(menu==1):
        sisi=int(input("Masukkan sisi : "))
        a=Kubus(sisi)
    elif(menu==2):
        panjang=int(input("Masukkan panjang : "))
        lebar=int(input("Masukkan lebar : "))
        tinggi=int(input("Masukkan tinggi : "))
        a=Balok(panjang, lebar, tinggi)
    elif(menu==3):
        jari=int(input("Masukkan jari-jari : "))
        tinggi=int(input("Masukkan tinggi : "))
        a=Tabung(jari, tinggi)
    elif(menu==4):
        jari=int(input("Masukkan jari-jari : "))
        tinggi=int(input("Masukkan tinggi : "))
        a=Kerucut(jari, tinggi)
    os.system('cls')
    if(menu>=1 and menu<=4):
        print("=======================")
        print("Luas = "+str(a.hitung_luas()))
        print("Volume = "+str(a.hitung_volume()))
        print("=======================")
        try:
            input("Tekan Enter untuk melanjutkan...")
        except SyntaxError:
            pass
