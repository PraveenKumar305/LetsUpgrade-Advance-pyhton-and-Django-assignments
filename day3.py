list1 = [(10,4),(90,3),(9,1),(10,4),(9,5)]


print(sorted(list1, key = lambda x:x[0] + x[1])) 

############################


list1 = [1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]

list1.sort()
print(list1)
list1.remove(0)
list1.remove(0)
list1.remove(0)
list1.remove(0)
list1.remove(0)
list1.remove(0)

list1.append(0)
list1.append(0)
list1.append(0)
list1.append(0)
list1.append(0)
list1.append(0)
print(list1)

#############################

list3 = ["192.168.10.9", "192.168.10.4", "192.168.10.11", "192.168.10.35"]


print(sorted(list3, key = lambda x:x[1])) 




