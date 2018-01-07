
class A:
    pass

class B:
    pass

class C(object):
    pass

class D(object):
    pass

def main():
    a=A()
    b=B()
    c=C()
    d=D()
    print(type(a))
    print(type(b))
    print(type(a)==type(b))
    print("-----------")
    print(type(A))
    print(type(B))
    print(type(A)==type(B))
    print("-----------")
    print(type(c))
    print(type(d))
    print(type(c) == type(d))
    print("-----------")
    print(type(C))
    print(type(D))
    print(type(C) == type(D))
    print("-----------")

if __name__ == '__main__':
    main()