#Assignment on loops
#July 22, 2018

#Problem 1
x = -11
if x <-20:
    print("x is less than -20")
elif x == -20:
    print("x is -20")
elif x > -20:
    print("x is greater than -20")
else:
    print("x does not exist")


#Problem 2
brange = range(2, 16)
for i in brange:
    if i % 3==0:
        print(i)
    else: continue

brange = range(2, 16)
for i in brange:
    if i % 3 ==0:
        print(i)
        break

#Problem 3
x = 97
while x <= 101:
    print(x)
    x += 1

#Problem 4
for i in range(5):
    pass

