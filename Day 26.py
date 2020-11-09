SHALLOW COPY
*****************************************

list=['xy',56,'z',100]
list1=['xyz',564,23,'a']
list2=list[:]
print(list)
print(list2)
print(id(list2))
print(id(list))



DEEP COPY
***************************************

from copy import deepcopy
list3=[['sujitha'],100,56,['reddy']]
list4=deepcopy(list3)
print(list4)
list3.append(5)
print(list3)
print(list4)

list3[0].append('bandi')
print(list3)
print(list4)

list4[0].append('bandi')
print(list3)
print(list4)
