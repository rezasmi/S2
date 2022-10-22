import random
a=random.randint(1,100)
print(a)
c=input()
e=100
f=1
while c!="d":
    if c=="k":
        h=random.randint(a,e)
        f=a
        a=h
        print(h)
        break
    if c =="b":
        h=random.randint(f,a)
        e=a
        a=h
        print(h)
        c=input()
        break
print("yeah")