from math import gcd

class Fraction:
    def __init__(self, numerateur, denominateur):
        self._num = numerateur
        self._denom = denominateur

    def __str__(self) :
        return f"{self._num}/{self._denom}"


    def addition (self, autre) :
        num = self._num * autre._denom + autre._num * self._denom
        denom = self._denom * autre._denom
        return Fraction(num, denom)

    def mult (self, autre) :
        num = self._num * autre._num
        denom = self._denom * autre._denom
        return Fraction(num, denom)

    def simplify(self):
        a = gcd(self._num, self._denom)
        num = self._num // a
        denom = self._denom // a
        if denom == 1 :
            return num
        else :
            return Fraction(num,denom)

    def app(self):
        return self._num/self._denom


def H(n):
    H = Fraction(0, 1)
    for i in range (1, n+1):
        H = H.addition(Fraction(1, i))
    return H.simplify()


def L(n):
    L = Fraction(0, 1)
    for i in range (0, n+1):
        if i % 2 == 0 :
            L = L.addition(Fraction(1, 2*i + 1))
        else :
           L = L.addition(Fraction(1, -2*i - 1))
    return L.app()


c = Fraction(10, 5)
assert(c.simplify() == 2)
print (c)
##
class Polynomial:
    def __init__(self, coefficients):
        self._coeffs = coefficients
        self._degre = self.get_deg()

    def get_deg(self):
        m = "-inf"
        for i in range(len(self._coeffs)):
            if self._coeffs[i]!= 0:
                m = i
        self.degre = m
        return m


    def __str__(self):
        s = ""
        for i in range(self._degre, 0, -1):
            if self._coeffs[i] != 0:
                s += f"{self._coeffs[i]} X**{i}"
                if i != 1 or (i == 1 and self._coeffs[0] != 0):
                    s += " + "
        if self._coeffs[0] != 0:
            s += f"{self._coeffs[0]}"
        return s

    def __add__(self, other):
        if len(other._coeffs) >len(self._coeffs):
            liste = other._coeffs[:]; n = len(self._coeffs)
        else: liste = self._coeffs[:]; n = len(other._coeffs)
        for i in range(n):
            liste[i] = self._coeffs[i] + other._coeffs[i]
        return Polynomial(liste)

    def __deriv__(self):
        liste = [0]*len(self._coeffs)
        for i in range(self._degre):
            liste[i] = self._coeffs[i + 1]*(i + 1)
        return Polynomial(liste)

    def __integrate__(self, C):
        liste = [0]*(len(self._coeffs) + 1)
        for i in range(1, self._degre + 2):
            liste[i] = Fraction(self._coeffs[i - 1],  i).simplify()
        liste[0] = C
        return Polynomial(liste)


d = Polynomial([3, 1, 1])
e = Polynomial([1, 2, 3])
print(d)
print (d.__add__(e))
print(d.__integrate__(2))







































