number=10
ans=''
while number!=0:
    tmp=number%2
    var=str(tmp)
    ans=var+ans
    number=number//2
print(ans)