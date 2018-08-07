#Monica Erdman
#Aug. 7, 2018
#String Operations Writing Assignment

#1. Perform appropriate operations to remove space and ; from string1 
#where string1 = " it rained a lot ;"
string1 = " it rained a lot ;"
print(string1.strip(' ;'))

#2. If list1 = ["we", "are", "going", "bowling"], 
#how would you get "we are going bowling"?
list1 = ["we", "are", "going", "bowling"]
print(" ".join(list1))

#3. If string2 = "programming; in Python; is fun". 
#Perform the required operations(s) to get ["programming", "in Python", "is fun"]
string2 = "programming; in Python; is fun"
str2 = string2.rsplit('; ')
print(str2)

#4. If w = "Anthem", convert w to uppercase. 
#Use find method to locate the index where "TH" appears in w.
w = "Anthem"
W = w.upper()
index = W.find('TH')
print(index)
