d={} 
print('Dictionary',d) 
n = int(input('Enter number of elements in dictionary')) 
for i in range(0,n): 
    d[i+1]=i+1 
print('Items in dictionary') 
for i in d.items():#items() return the key,value tuples 
    print(i) 
print('Sum of values in dictionary=',sum(d.values()))