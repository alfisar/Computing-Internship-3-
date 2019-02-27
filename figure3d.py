from math import sqrt,pi
class Kubus():
    
    jumlah_sisi = 12

    def __init__(self,sisi):
        self.sisi = sisi
    
    def hitung_volume(self):
        x = self.sisi
        return x*x*x
    
    def hitung_luas(self):
        x = self.sisi
        return 4*x*x

pass

class Balok():
    
    jumlah_sisi = 12

    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_volume(self):
        return self.panjang*self.lebar*self.tinggi
    
    def hitung_luas(self):
        p = self.panjang
        l = self.lebar
        t = self.tinggi
        return 2*(p*l + p*t + l*t)

pass

class Tabung():
    
    jumlah_sisi = 3

    def __init__(self,jarijari,tinggi):
        self.jarijari = jarijari
        self.tinggi = tinggi
    
    def hitung_volume(self):
        return (self.jarijari*self.jarijari*self.tinggi*pi)
    
    def hitung_luas(self):
        return (2*self.jarijari*self.jarijari*pi + 2*self.jarijari*pi*self.tinggi)

pass

class Kerucut():
    
    jumlah_sisi = 2

    def __init__(self,jarijari,tinggi):
        self.jarijari = jarijari
        self.tinggi =  tinggi 
    
    def hitung_volume(self):
        return (self.jarijari*self.jarijari*self.tinggi*pi)/3
    
    def hitung_luas(self):
        r = self.jarijari
        t = self.tinggi
        return (pi*r*r + pi*r*(sqrt((r*r)+(t*t))))

pass