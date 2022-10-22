def divisor(vorodi):

    c=1       

    for i in range(1,vorodi):             

        if (vorodi%i==0):                             

            c+=1   
    return c

list1=[]
list2=[]
adad=()
for adad in range(20):
    adad=int(input())
    adad2=divisor(adad)
    list1.append(adad)
    list2.append(adad2)
    #print(list1)
   # print(list2)

print(max(list1),max(list2)) 
#print(max(list2))


