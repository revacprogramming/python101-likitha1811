fhandle = open('mbox-short.txt')
count = 0
#add = list()
for line in fhandle:
    if line.startswith('From'):
        list = line.strip()
        list = line.split()
        if list[0] == 'From:':
            continue
        print(list[1])
        count = count + 1
        #add.append(list[1])
#print('There were',len(add),'lines in the file with From as the first word')
print('There were',count,'lines in the file with From as the first word')