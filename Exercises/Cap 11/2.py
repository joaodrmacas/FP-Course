from math import gcd
class racional():
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def __repr__(self):
        d = gcd(self.nume(),self.deno())
        return "{}/{}".format(self.nume()//d,self.deno()//d)

    def nume(self):
        return self.num
    def deno(self):
        return self.den
    def __add__(self, other):
        return racional(self.nume() * other.deno() + self.deno() * other.nume(), self.deno() * other.deno())
    def __mul__(self, r2):
        return racional(self.nume() * r2.nume(), self.deno() * r2.deno())

r1 = racional(2,4)
r2 = racional(1,6)
print(r1)
print(r2)
print(r1 + r2)
print(r1*r2)