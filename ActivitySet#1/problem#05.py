# Functions


def computepay(hrs, r):
   if hrs<40:
    print("",hrs*r)
   else:
    return(hrs*r+((hrs-40)*r*0.5))
    
hrs = float(input())
r= float(input())
 
p = computepay(hrs, r)
print("Pay", p)
