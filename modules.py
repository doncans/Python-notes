class A:
    var = 100
    def meth1(self):
        print('Class A Method')
class B(A):
    var1 = 200
    def meth2(self):

        
        print('Class B method')
class C(B):
    var2 = 300
    def meth3(self):
        print('Class C Method')

'''Method resolution order'''
class Vehicle:
    def __init__(self, fuel, breaks, wheel):
        self.fuel = fuel
        self.breaks = breaks
        self.wheel = wheel

    def two_wheeler(self, seating_capacity):
        self.seating_capacity = \
            seating_capacity

    def three_wheeler(self, seating_capacity):
        self.seating_capacity=\
            seating_capacity

obj1 = C()
obj = Vehicle('Petrol', 'yes', 4)

