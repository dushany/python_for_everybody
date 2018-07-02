# open mbox-short.txt
# parse From line and print email addresses
# print count at end

f_name = input("Enter file name: ")
f_head = open(f_name)
count = 0
for line in f_head:
    if line.startswith("From "):
        ch = line.split()
        print(ch[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
