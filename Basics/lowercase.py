filename = input('Enter a filename ')  
infile = open(filename)  
words = []  
for line in infile:  
    temp = line.split()      
    for i in temp:          
        words.append(i)     
infile.close()  
words.sort()  
 
for i in words:      
    print(i.lower()) 