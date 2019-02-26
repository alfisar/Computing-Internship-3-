from math import sqrt,pi

class Segitiga:
    jumlah_sisi = 3
    pass

class Segiempat:
    jumlah_sisi = 4
    pass

class Samasisi(Segitiga):

    def __init__(self,sisi,tinggi):
        self.sisi = sisi
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return (self.sisi*self.tinggi/2)
    
    def hitung_keliling(self):
        return 3*self.sisi

    pass

class Samakaki(Segitiga):

    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return self.alas*self.tinggi/2
    
    def hitung_keliling(self):
        a = self.alas
        t = self.tinggi
        return a+(2*sqrt((t*t)+(a*a/4)))

    pass

class Persegi(Segiempat):
    
    def __init__(self, panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang*self.lebar
    
    def hitung_keliling(self):
        return 2*(self.panjang+self.lebar)

    pass

class Trapesium(Segiempat):
    
    def __init__(self, alas,tutup, tinggi):
        self.alas =  alas
        self.tutup = tutup
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return (self.alas+self.tutup)*self.tinggi/2

    def hitung_keliling(self):
        a = self.alas
        x = self.tutup
        t = self.tinggi
        return a+x+2*(sqrt((a-x)*(a-x) + (t*t)))
    
    pass
 
class Jajargenjang(Segiempat):
     
    def __init__(self,alas,tinggi):
         self.alas = alas
         self.tinggi = tinggi
    
    def hitung_luas(self):
        return self.alas*self.tinggi
    
    def hitung_keliling(self):
        return 2*(self.alas+self.tinggi)

    pass
