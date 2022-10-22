my_list1=[]
my_list2=[]
sen1=()
while sen1!=-1:
    sen1=int(input())
    my_list1.append(sen1)
    my_list2.append(sen1)
max1=int(max(my_list1))
#print(type(max1))
#print(type(my_list1))
#print(type(my_list2))
my_list2.remove(max1)
max2=int(max(my_list2))
print(max1,max2)