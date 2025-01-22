#Program to show aliasing and side effects
list1=[10,23,55]
list2=list1         #refers to same memory location 
print({id(list1)})
print({id(list2)})
print("list 1: ",list1)
print("list 2: ",list2) 
print("Changing element '23' of List 1")
list1[1]=99
print(list1)
print(list2)        #automatically element '23' in list2 also changes