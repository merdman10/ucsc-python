#Monica Erdman
#Aug. 21, 2018
#Reading and writing text files assignment 2

#1. What is the difference between write() and writelines()?

#write() takes one argument and writelines() expects an iterable (list, tuple, string, etc.)

#2. What are the advantages of using "with" context manager when opening a file?
#Using the with keyword properly closes the text file when you're done working with it. It prevents a leaking file descriptor. If you don't use the with keyword when opening a text file, you should make sure to call fd.close() at the end of your code.
