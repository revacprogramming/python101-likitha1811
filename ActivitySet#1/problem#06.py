# Loops & Iterators

large = None
small = None
while True:
    n = input()
    if (n == "done"):
        break
    try:
        num=int(n)
    except:
        print("Invalid input")
        continue
    if small is None:
        small=num
    elif(small>num):
        small=num
                        
    if large is None:
        large=num
    elif(large<num):
        large=num
        continue
              
print("Maximum is",large)
print("Minimum is",small)
      
