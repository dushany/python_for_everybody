# read through file and determine who has sent the greatest
# number of mail messages

f_name = input("Enter file name: ")
f_head = open(f_name)
my_dict = dict()

# loop through text and extract emails and count
for line in f_head:
    if line.startswith('From '):
        words = line.split()
        my_dict[words[1]] = my_dict.get(words[1],0) + 1

# determine most prolific email and its count
top_count = None
top_email = None

for name, count in my_dict.items():
    if top_count is None or count > top_count:
        top_email = name
        top_count = count
print(top_email,top_count)
