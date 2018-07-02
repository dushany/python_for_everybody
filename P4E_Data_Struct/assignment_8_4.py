# open romeo.txt and read each line
# build list of unique words

f_name = input("Enter file name: ")
f_head = open(f_name)
f_text = f_head.read()
lst = list()
ch = f_text.split()
for i in ch:
    if i in lst:
        continue
    else:
        lst.append(i)
lst.sort()
print(lst)
