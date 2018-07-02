# read through file and determine count of
# hours for each message.

f_name = input("Enter file name: ")
if len(f_name) < 1 :
    f_name = "mbox-short.txt"
f_head = open(f_name)

# loop through text and extract hour and count
dct = dict()
for line in f_head:
    if line.startswith('From '):
        words = line.split()
        tmp = words[5].split(":")
        dct[tmp[0]] = dct.get(tmp[0],0) + 1

lst = list()
for k,v in dct.items():
    tup = (k,v)
    lst.append(tup)
    lst = sorted(lst)

for k,v in lst:
    print(k,v)
