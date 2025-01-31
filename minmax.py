#Function to Find min and max value from a list without using min and max func
def minmax(numlist):
    length=len(numlist)
    min=max=numlist[0]
    for i in numlist[1:]:
        if i<min:
            min=i
        if i>max:
            max=i
    print('Largest Number:',max)
    print('Smallest Number:',min)
numlist=list(map(int, input('Enter Numbers (Separated using Comma): ').split(",")))
print(numlist)
minmax(numlist)