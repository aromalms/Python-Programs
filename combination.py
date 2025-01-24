#program to perform combination equation (nCr)
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))
n=(int(input("Enter values of 'n': ")))
r=(int(input("Enter values of 'r': ")))
if r > n:
    print("Invalid input: 'r' cannot be greater than 'n'")
else:
    x=factorial(n)
    y=factorial(n-r)
    z=factorial(r)
    res=x/(y*z)
    print(res)
