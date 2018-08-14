#Monica Erdman
#Aug. 14, 2018
#Error handling writing assignment

#1. t1 = (10, 11, 12). Perform t1+7 and explain message.
t1 = (10, 11, 12)
#t_2 = t1 + 7 #Throws TypeError because tuples can only concatenate tuples (not integers)

#2. Write try-except to handle the above tuple concatenation. If there is a problem, then t1 should be concatenated with t2 = (7,) and the result should be stored in t3.
try:
    t3 = t1 + 7
    print(t3)
except:
    t2 = (7,)
    t3 = t1 + t2
    print("t3:", t3)

#3. Write try-except-else-finally to implement problem 2 so that there is a message in else clause, and the final value of t3 will be printed by the finally clause.
try:
    t3 = t1 + 7
except:
    t2 = (7,)
    t3 = t1 + t2
else:
    print("No exception thrown")
finally:
    print("t3:",t3)

#4. Handle index error for list1 = [11, 14, 16] using try-except. If the user is accessing an index 6, then you should print "Item at index 6 is not found".
list1 = [11, 14, 16]
try:
    l6 = list1[6]
except IndexError:
    print("Item at index 6 is not found")

