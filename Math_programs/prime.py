n=int(input('Enter n value: ')) 
for i in range (2,n): 
    count=0 
    for num in range (2,i//2+1): 
        if(i%num ==0): 
            count+=1 
    if(count==0): 
        print(i,"is prime number")