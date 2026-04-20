l=[1,2,3,4,5] 
l.append(6) 
print(l)  
l.append([5,6,7])  
L=[1,2,3,4,5,6,[5,6,7]] 
del( L[3]) 
print(L) # [1,2,3,5,6,[5,6,7]] 
L.remove(5) #[1,2,3,6,[5,6,7]] 
print("After removal",L) 
l.reverse() 
print("After reverse",l) 
l.pop() 
print("After pop",l) 
l.insert(4,[5,6]) 
print("After insertion",l) 
l2=l.copy() 
print("After copying",l2) 