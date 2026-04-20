m = int(input('Enter number of rows in matrix 1:'))  
n = int(input('Enter number of columns in matrix 1:'))  
p = int(input('Enter number of rows in matrix 2:'))  
q = int(input('Enter number of columns in matrix 2:'))  
 
if (n != p):  
    print('Matrix multiplication is not possible')  
else:      
    a = []      
    b = []      
    print('Enter Elements in Matrix A')  
    for i in range(m):  
        temp = []          
        for j in range(n):              
            temp.append(int(input()))  
        a.append(temp)      
    print('Enter Elements in Matrix B')      
    for i in range(p):  
        temp = []          
        for j in range(q):              
            temp.append(int(input()))  
        b.append(temp)      
    res = []      
    for i in range(m):  
        temp = []          
        for j in range(q):  
            sum = 0              
            for k in range(n):                  
                sum = sum + a[i][k] * b[k][j]              
            temp.append(sum)          
        res.append(temp)      
    print('Resultant Matrix:')      
    for i in range(m):          
        for j in range(q):  
            print(res[i][j], end=' ')          
        print()