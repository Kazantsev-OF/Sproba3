def proba(a,b,c):
    if a > b:
        print("good a greater than b")
    elif a == b:
        print("sorry a and b are equal")
        a = a + c
        if a > b:
            print('good a greater than b')
        elif a == b:
            print("sorry a and b are equal")
    else:
        print("it is fail. a still less b")
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

proba(a,b,c)
