from Pets import *
import os
temp = False
masukan = ''
while (masukan != '0'):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================")
    print("1. Mendaftarkan Pets")
    print("2. Check lapar")
    print("3. Siapa saja yang lapar")
    print("4. kasih makan ")
    print("5. Bersusara ")
    print("6. Spesies ")
    print("0. Exit")
    print("=======================")
    masukan = input()

    if (masukan == '1'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=======================")
        print("1. Kucing")
        print("2. Dog")
        print("3. Burung")
        print("=======================")

        print("Nama : ",end='')
        nama = input()
        print("Umur : ", end='')
        umur = input()
        print("Jenis : ", end='')
        jenis = input()
        if (jenis == "1"):
            a = Kucing(nama,umur)
        elif(jenis == "2"):
            a = Dog(nama,umur)
        elif(jenis == "3"):
            a = Burung(nama,umur)
        b = pet(a)

    elif(masukan == '2'):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(b.is_hungry())
        input()
    
    elif(masukan == '3'):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(b.whos_hungry())
        input()  

    elif(masukan == '4'):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Nama : ",end='')
        nama = input()
        b.pet_list = a.eat(b.pet_list,nama)
    
    elif(masukan == '5'):
        os.system('cls' if os.name == 'nt' else 'clear')

        a.sound()
        input()
    
    elif(masukan == '6'):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(a.spesies)
        input()