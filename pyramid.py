#printing pyramid pattern
n=int(input("Enter Value of 'n': "))
for i in range(1,n+1):
    print(" "*(n-i)+ "* "*i)