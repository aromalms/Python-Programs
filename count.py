def check(str):
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper+=1
        else:
            lower+=1   
    return upper,lower
s='KoTTayam'
up,low=check(s)
print('Number of Uppercase letters:',up,'\nNumber of Lowercase letters:',low)