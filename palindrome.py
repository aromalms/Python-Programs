#program to check whether a number is palindrome or not
number=int(input("Enter the Number: "))
temp=number
ans=0
while number!=0:
    var=number%10
    ans=ans*10+var
    number=number//10
if(temp==ans):
    {
    print("Number is palindrome")
    }
else:
   {
      print("Number is not Palindrome")
   }


