# Read through and parse a file with text and numbers.
# You will extract all the numbers in the file and
# compute the sum of the numbers.

import re

f_name = input("Enter file name: ")
if len(f_name) < 1 :
    f_name = "regex_sum_52857.txt"
f_head = open(f_name)

lst = list()
for line in f_head:
     lst.extend(re.findall("[0-9]+",line))
lst = [int(i) for i in lst]
print(sum(lst))

# alternate way to get answer
# print(sum([int(i) for i in re.findall("[0-9]+",f_head.read())]))
