class vehicle:
    def __init__(self,year,price):
        self.year = year
        self.price = price
    
    pass

class Car(vehicle):
    wheel_count = 4
    capacity = 4
    
    def pay_tax(self):
        return 0.15*self.price

    def park(self,hour):
        biaya = 1250*self.wheel_count*hour
        if(self.capacity > 5):
            biaya += 5000
        return biaya

    pass

class Motorbike(vehicle):
    wheel_count = 2
    capacity = 2
    
    def pay_tax(self):
        return 0.1*self.price

    def park(self,hour):
        biaya = 1250*self.wheel_count*hour
        if(self.capacity > 5):
            biaya += 5000
        return biaya

    pass

class Bicycle(vehicle):
    wheel_count = 2
    capacity = 1
    
    def pay_tax(self):
        return 0

    def park(self,hour):
        biaya = 1250*self.wheel_count*hour
        if(self.capacity > 5):
            biaya += 5000
        return biaya
    pass
