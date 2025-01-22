#Program to overcome the side effects of aliasing
list1=[10,23,55]
list2=[]        #refers to diff memory location 
print({id(list1)})
print({id(list2)})
list2.extend(list1)
print("list 1: ",list1)
print("list 2: ",list2) 
print("Changing element '23' of List 1")
list1[1]=99
print("list 1: ",list1)
print("list 2: ",list2)        #element '23' in list2 remains same