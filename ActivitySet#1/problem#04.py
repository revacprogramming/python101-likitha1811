# Conditional Execution

hrs = float(input())
r=float(input())
if hrs<40:
    print("",hrs*r)
else:
   
    print(*"",hrs*r+((hrs-40)*r*0.5))
