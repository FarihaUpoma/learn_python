import re

# Your code goes here

my_list = []
for x in dir(re):
    if "find" in x:
        my_list.append(x)
        
print((my_list))
