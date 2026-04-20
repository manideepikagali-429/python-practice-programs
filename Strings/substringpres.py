x=input("Enter the main string") 
y=input("Enter the substring") 
z=x.find(y) 
if(z==-1): 
    print("Substring not found") 
else: 
    print("Substring found at",z)