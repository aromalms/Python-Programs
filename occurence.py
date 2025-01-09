String="Hello"
limit=len(String)
x="l"
count=0
for i in range(0,limit):
    if(x==String[i]):
        count+=1
print(count)