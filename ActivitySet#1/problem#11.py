# Tuples

filename = "dataset/mbox-short.txt"
name = input("Enter file:")

if len(name) < 1:

    name = "mbox-short.txt"

counts = {}

handle = open(name)

for line in handle:

    if not line.startswith('From '):

        continue

    svi = line.replace(':',' ')

    words = svi.split()

    pu = words[5:6]

    for word in pu:

        counts[word] = counts.get(word,0) + 1

lst = []

for k,v in sorted(counts.items()):

    tuk = (k,v)

    lst.append(tuk)

ki = sorted(lst)    

for k,v in ki:

    print(k,v)