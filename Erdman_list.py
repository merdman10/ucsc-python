#Monica Erdman
#Aug. 13, 2018
#Lists, tuples, and dictionaries assignment

#1. If list1 = [14, 23, 27, 32], reverse the elements in list1 and print list1.
list1 = [14, 23, 27, 32]
list1.reverse()
print(list1)

#2. If list2 = [13, 19, 27, 35, 37, 12], perform the following sequentially an dafter every operation print the list:
#2a. Sort list2
#2b. Pop element at index 2.
#2c. Insert value of 25 at index 2
#2d. Append 10 to list2
#2e. Clear elements from list2
list2 = [13, 19, 27, 35, 37, 12]
print("Original list2:",list2)
list2.sort()
print("Sorted:",list2)

list2.pop(2)
print("Popped [2]:",list2)

list2.insert(2, 25)
print("Insert 25:",list2)

list2.append(10)
print("Append 10:",list2)

list2.clear()
print("Cleared:",list2)
