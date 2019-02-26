class pet:
    pet_list = []
    def __init__(self,animal):
        self.pet_list.append(animal)
    
    def is_hungry(self):
        temp = False
        i = 0
        while (temp == False) and (i < len(self.pet_list)):
            if(self.pet_list[i].hungry == True):
                temp = True
            i += 1
        return temp
    
    def whos_hungry(self):
        j = len(self.pet_list)
        for i in range(j):
            if(self.pet_list[i].hungry == True):
                print(self.pet_list[i].name)

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hungry = True

    def eat(self,b,nama):
        i = 0
        while(i <= len(b)) and (b[i].name != nama):
            i+=1
        b[i].hungry = False
        return b

class Kucing(Animal):
    spesies = "Felis catus"
    def __init__(self,name,age):
        Animal.__init__(self,name,age)
        print(self.spesies)

    def sound(self):
        print("Miaw")

class Dog(Animal):
    spesies = "Canis domesticus"
    def __init__(self,name,age):
        Animal.__init__(self,name,age)
        print(self.spesies)

    def sound(self):
        print("Gorf Gorf")

class Burung(Animal):
    spesies = "Chordata"
    def __init__(self,name,age):
        Animal.__init__(self,name,age)
        print(self.spesies)

    def sound(self):
        print("Cicicuit")


