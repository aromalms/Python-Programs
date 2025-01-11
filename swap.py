#swap two numbers without using a third variable(with function)
def swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b
a=int(input("Enter Value of A : "))
b=int(input("Enter Value of B : "))
print("Value of A and B Before Swapping")
print("A=",a," B=",b)
a,b=swap(a,b)
print("Value of A and B After Swapping")
print("A=",a, " B=",b)

