d={} 
print('Dictionary',d) 
d[1]=4 
d[2]=5 
d[3]=6 
print('Keys in dictionary') 
for i in d.keys():#keys() return the keys in the dictionary 
    print(i) 
print('Values in dictionary') 
for i in d.values(): 
    print(i) 
print('Items in dictionary') 
for i in d.items():#items() return the key,value tuples 
    print(i)