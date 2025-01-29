#sorting keys in a dictionary
dict={'hello':2,'good':1,'afternoon':3}
keys=list(dict.keys())
keys.sort()
print(keys)
sorted_dict={i:dict[i] for i in keys}
print(sorted_dict)