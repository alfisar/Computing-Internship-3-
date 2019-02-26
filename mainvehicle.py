from vehicle import *
import os

menu=int
while(menu!=0):
    menu2 = int
    os.system('cls')
    print("=======================")
    print("Pilih Jenis Kendaraan")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    print("")
    print("")
    print("0. Exit")
    print("=======================")
    menu=int(input())
    if(menu!=0):
        os.system('cls')
        print("=======================")
        print("Masukkan data kendaraan berikut")
        print("Tahun : ")
        year=int(input())
        print("Harga : ")
        price=int(input())
        print("=======================")
        if(menu==1):
            a=Car(year, price)
        elif(menu==2):
            a=Motorbike(year, price)
        elif(menu==3):
            a=Bicycle(year, price)
        else:
            menu2=0
        while(menu2!=0):
            os.system('cls')
            print("=======================")
            print("1. Hitung Biaya Parkir")
            if(menu!=3):
                print("2. Tampilkan Pajak Kendaraan")
            print("")
            print("")
            print("0. Kembali ke Awal")
            print("=======================")
            menu2=int(input())
            os.system('cls')
            print("=======================")
            if(menu2==1):
                print("Masukkan Durasi Parkir = ")
                hour = int(input())
                os.system('cls')
                print("=======================")
                print("Biaya Parkir = " + str(a.park(hour)))
            elif(menu2==2):
                print("Biaya Pajak = " + str(a.pay_tax()))
            try:
                input("Tekan Enter untuk melanjutkan...")
            except SyntaxError:
                pass