#Monica Erdman
#Aug. 7, 2018
#String Operations Assignment

#1. If w = "equation", a. Slice first three characters from w and assign it to w1 and print w1.
#b. Do the necessary operations so that the output will be "EQUAtion"
w = "equation"
w1 = w[0:3]
print(w1)

w2 = w[0:4].upper()+w[4:]
print(w2)

#for i,j in enumerate(w):
#    if i < 4:
#        print(j.upper())
        
        
#    else:
#        continue
        #w2.append()

#2. t = "programming is fun". Slice t into three parts.
#Then do the required to get the following:
# "Programming IS fun"

t = "programming is fun"
ts = t.split()
t1 = ts[0].capitalize()
t2 = ts[1].upper()
t3 = ts[2]
t_full = (t1,t2,t3)
print(" ".join(t_full))


