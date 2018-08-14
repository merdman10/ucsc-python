#Monica Erdman
#Aug. 13, 2018
#Lists, tuples, and dictionaries writing assignment

#a. Perform the following operations on list1 = [-11, -4, 5, 12, 13, 14, 19]
#a1. Find the number of elements in list1
#a2. Append 22 to list1
#a3. Pop element from index 3. Print the popped element as well as list1.
#a4. Convert the list to tuple. Then print the tuple.
list1 = [-11, -4, 5, 12, 13, 14, 19]
print("Length of list1:",len(list1))
list1.append(22)
print("Updated length of list1:",len(list1))
p = list1.pop(3)
print('Popped element: {} \nNew list1: {}'.format(p, list1))

tup_l1 = tuple(list1)
print("Convert to tuple:",tup_l1)

#b. If t1 = (3, 6, 7, 11) perform all the following operations:
#b1. Find the number of elements in t1.
#b2. Concatenate t1 to t2 = (1, 2) and create t3
#b3. If possible, append -4 to t3. If not, explain why.
t1 = (3, 6, 7, 11)
t2 = (1, 2)
print("Length of t1:", len(t1))
t3 = t1 + t2
print("t3:", t3)
t3.append(-4) #Cannot append to a tuple; tuples are immutable

#c. Create a dictionary with 5 key-values so that state is the key and its capital is the value. Print the dictionary.
d = {"CA": "Sacramento", "MD": "Baltimore", "TX": "Austin", "VA": "Richmond", "AZ": "Phoenix"}
print(d)

#d. If dictionary1 = {12: "Amazon", 14: "Nvidia", 15: "Tesla"}, perform required operations to get the following. If you can't perform a specific operation, explain why.
#d1. The length of the dictionary?
#d2. The value for 14?
#d3. Print the keys and values as lists.
#d4. Value for dictionary1[16].
dictionary1 = {12: "Amazon", 14: "Nvidia", 15: "Tesla"}
len(dictionary1) #valid
dictionary1[14] #valid
print("Keys:",list(dictionary1.keys()),"\nValues:", list(dictionary1.values())) #valid
dictionary1[16] #invalid; there is no key 16 in dictionary1
