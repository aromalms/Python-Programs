#factorial using recursion(function calling itself)
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))
n=(int(input("Enter values of 'n': ")))
print(factorial(n))
