from math import pow
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return complex(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return complex(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        return complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __div__(self, other):
        try: 
            return self.__mul__(complex(other.real, -1*other.imag)).__mul__(complex(1.0/(other.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None
    def mod(self):
        return complex(pow(self.real**2+self.imag**2, 0.5), 0)
    def __str__(self, precision=2):
        return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'

    
A = complex(*map(float, raw_input().strip().split()))
B = complex(*map(float, raw_input().strip().split()))

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A.mod())
print(B.mod())