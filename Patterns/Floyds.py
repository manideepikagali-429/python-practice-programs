n=int(input("Enter no of rows:"))
print("Floyds triangle")
a=1
for i in range(1,n+1):
    for j in range(i):
        print(a,end=" ")
        a=a+1
    print()
