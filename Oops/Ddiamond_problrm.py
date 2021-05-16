class A:
    def print_show(self):
        print('this is a methiod foe clas  A')

class B(A):
    def print_show(self):
        print('this is a methiod foe clas  B')

class C(A):
    def print_show(self):
        print('this is a methiod foe clas  C')
class D(B,C):
    def print_show(self):
        print('this is a methiod foe clas  D')


a= A()
b=B()
c =C()
d =D()


print(d.print_show())