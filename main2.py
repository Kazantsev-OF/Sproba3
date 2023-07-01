def proba(a,b,c):
    while a < b:
        print(a,"<",b)
        a += c
    print("Yes", a, ">", b)

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

proba(a,b,c)
