#binary to decimal
bnumber=input("Enter Number: ")
decnum=0
exp=len(bnumber)-1
for digit in bnumber:
    decnum=decnum+int(digit)*2**exp
    exp-=1
print("Decimal Number:",decnum)