#Functions writing assigment
#Monica Erdman
#July 30, 2018

#Problem 1
def raised_function(v1, v2): 
    '''
    Takes 2 values v1 and v2, and computes v1 raised to v2.
    Returns the value.
    '''
    
    print("In raised_function(): v1: {}, v2: {}".format(v1, v2))    #print inputs
        
    result = v1**v2         #defines result as v1 raised to v2
    
    print("In raised_function(): v1: {}, v2: {} result: {}".format(v1,v2, result))
    
    return  result            # computes v1 raised to v2 and returns the value

# test code
print(raised_function.__doc__)
ret = raised_function(4,0)

#run code
ret = raised_function(4,7)
print("raised_function({},{}), returns: {}".format(4,7,ret))

print("Function worked?", ret == 4**7)

#Problem 2
def string_loop(strIn):
    '''
    Takes a string strIn and loops through it and prints the vowels in the string
    '''

    print("In string_loop(): strIn: {}".format(strIn)) #print input

    result = []
    for i in strIn:
        if i in "aeiouAEIOU":
            result.append(i)
    
    print("In string_loop(), result: {}".format(result))
    return result

#test code
print(string_loop.__doc__)
ret = string_loop("aeiou")
ret = string_loop("AEIOU")
ret = string_loop("123456")
ret = string_loop("spam and eggs")
ret = string_loop("")

#run code
ret = string_loop("compute")

#Problem 3
def string_len(s1 = "apples"):
    '''
    Takes a default value s1 = "apples" and prints the length of the string
    '''

    print("In string_len(): s1: {}".format(s1)) #print input

    result = len(s1) #finds the length of s1

    print("String: {} Length: {}".format(s1, result))

#test code
string_len("1")
string_len("12")
string_len("")
string_len()

#run code
ret = string_len("watermelon")
print("Function worked?", len("watermelon") == ret)
