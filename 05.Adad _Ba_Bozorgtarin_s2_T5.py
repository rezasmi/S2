from fnmatch import fnmatch


def divisor(vorodi):

    c=1       

    for i in range(1,vorodi):             

        if (vorodi%i==0):                             

            c+=1       
    return c

list1=[]

adad=()
for adad in range(20):
        adad=int(input())    
        adad2=divisor(adad)
        list1.append((adad,adad2))


final = max(list1,key=lambda x:(x[1],x[0]))

print (final[0],final[1])