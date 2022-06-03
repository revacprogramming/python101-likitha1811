# Dictionaries

filename = "dataset/mbox-short.txt"
f_name = input("Enter File Name: ")
f_hand = open(f_name)
count = dict()

for line in f_hand:
    if line.startswith("From") and not line.startswith("From:") :
        message = line.rstrip().split()
        for sender in message:
            if sender == message[1]:
                count[sender] = count.get(sender,0) + 1

max_sender = None
max_num = None
for sender,num in count.items():
    if max_num is None or num > max_num :
        max_num = num
        max_sender = sender
print(max_sender, max_num)