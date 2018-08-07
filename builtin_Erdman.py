#Monica Erdman
#Aug. 6, 2018
#Built-in modules writing assignment

#1. Import math module and find the cosine of pi/4
import math
a = math.cos(math.pi/4)
print(a, "radians")

#2. From list2 = [6, 12, 15, 21], randomly choose an element. Then use the pow function from math module to determine that element raised to 3 and print it.
import random, math
list2 = [6,12,15,21]
for i in range(10):
    x = random.choice(list2)    #randomly chooses one element from list2
    power = math.pow(x,3)       #raises it to the 3
    print("{} raised to 3: {}".format(x,power)) #prints either 216, 1728, 3375, or 9261

#3. Seed using the current date and then generate a random number. Hint: use datetime.datetime.now().date() to obtain a date object and pass date object into random.seed.
import datetime, random
d = datetime.datetime.now().date()
random.seed(d)
for i in range(10):
    w = random.random
    print("Iteration", i, "Date =", w)

#4. Use time.clock() to find the time before and time after the for-loop that loops through range(1000) and appends the value to a list called list1. Print the time taken for the loop.
import time
list1 = []
start = time.time()
for i in range(1000):
    list1.append(i)
stop = time.time()
print("Time taken for loop: {}".format(stop-start))
