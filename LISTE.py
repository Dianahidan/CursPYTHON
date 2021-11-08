list1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

list2 = list1.copy()
list2.sort()
print(list2)

list2.reverse()
print(list2)

list3 = list2[-2:-10:-2] 
#poate fi si list3 = list2[::2]
print(list3)

list3 = list2[::-2]
print(list3)

list3 = list2[-3:-10:-3]
#poate fi si list3 = list2[1:9:3]
print(list3)
