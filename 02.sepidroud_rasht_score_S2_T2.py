my_list = []  # crerate a list to hold values read from input
wins=0
emtiaz_kol=0
for emtiaz in range(30):  # run this section 30 times
    emtiaz = int(input())  #  Reads an integer from input and saves it to inp variable
    my_list.append(emtiaz)  # append the read number to my_list
    if emtiaz==3:
      wins=wins+1
      emtiaz_kol=emtiaz_kol+3
    elif emtiaz==1:
        emtiaz_kol=emtiaz_kol+1
    elif emtiaz==0:
          emtiaz_kol=emtiaz_kol+0
print(emtiaz_kol,wins)



