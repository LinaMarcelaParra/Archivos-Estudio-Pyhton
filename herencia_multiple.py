class A:
    def	__init__(self):
        print('Soy de	clase A')

class B:
    def __init__(self):
        print('Soy de	clase B')

class C(A,B):
        pass

c= C()
