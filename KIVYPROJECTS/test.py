class Vehicle():

    def __init__(self, *args, **kwargs):
        self.name = 'murano'
        self.year = 2010

    def car_name(self):
        return self.name 
    def car_year(self):
        return self.year
vec = Vehicle()
print('this is the vehicle name', vec.car_name())

class Car(Vehicle):

    def car_name(self):
        super(Car, self).car_name()

c = Car()

print('this is the car name', c.car_name())