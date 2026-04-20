def strLength(string): 
    count=0 
    for i in string: 
        print(i) 
        count+=1 
    return count 
string=input('Enter a string') 
count=strLength(string) 
print('Length of string = ',count)