number=int(input("Enter the Number to be reversed: "))
String=str(number)
ans=0
while number!=0:
    var=number%10
    ans=ans*10+var
    number=number//10
print(ans)


