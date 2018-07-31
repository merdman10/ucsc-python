#Monica Erdman
#Functions assignment
#July 30, 2018

#Problem 1
def list_3and4(list1):
    '''
    Takes a list and returns values from the list that are divisible by both 3 and 4
    '''

    print("In list_3and4(): {}".format(list1))

    l2 = []
    for i in list1:
        if i % 3 ==0 and i % 4 ==0:
            l2.append(i)
        else:
            continue

    print("In list_3and4(), result: {}".format(l2))
    return l2

#test code
x = list_3and4(range(1,145,12))
print(x == [])
x = list_3and4(range(0,145,12))
print(x == [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144])

#run code
list1 = [21, 24, 27, 32, 36, 40]
x = list_3and4(list1)
print(x == [24, 36])


#Problem 2
def write_vowels(word):
    '''
    Takes a string and returns a list with the vowels from the word
    '''

    vowels = []
    for i in word:
        if i in "aeiouAEIOU":
            vowels.append(i)
    print("In write_vowels(): {}, Result: {}".format(word, vowels))
    return vowels

#test code
v = write_vowels("aeiou")
v = write_vowels("AEIOU")
v = write_vowels("san francisco")

#run code
v = write_vowels("totality")
