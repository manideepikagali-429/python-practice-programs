m = int(input('Enter number of rows in matrix 1:'))  
n = int(input('Enter number of columns in matrix 1:'))  
a = []  
print('Enter Elements in Matrix A')  
for i in range(m):  
    temp = []      
    for j in range(n):          
        temp.append(int(input()))  
    a.append(temp)  
  
print('Elements of array A')  
for i in range(m):      
    for j in range(n):  
        print(a[i][j], end=' ')      
    print()  
 
print('Transpose of elements')  
for i in range(n):      
    for j in range(m):  
        print(a[j][i], end=' ')      
    print()