import random
a = 1
b = 99 
hads = random.randint(a, b)
print (hads)
while True:
    javab = input()
    if javab == 'k':
        b = hads - 1
        hads = random.randint(a, b)
        print (hads)
    elif javab == 'b':
        a = hads + 1
        hads = random.randint(a, b)
        print (hads)
    elif javab == 'd':
        break