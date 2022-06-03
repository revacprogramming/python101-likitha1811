# Lists

filename = "dataset/romeo.txt"
file_name = input("Enter file name: ")
file_handling = open(file_name)
empty_list = list()
filled_list = list()

for line in file_handling:
    line = line.strip().split()
    for word in line:
        if word not in empty_list:
            empty_list.append(word)
            filled_list = sorted(empty_list)

print(filled_list)