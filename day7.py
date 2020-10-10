list1=[10,20,30,40,50]
list2=[5,15,25,35,45,60]

list3 = list1 + list2
print(list3)
new_list = []

while list3:
    minimum = list3[0]  # arbitrary number in list 
    for x in list3: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    list3.remove(minimum)    

print(new_list)
