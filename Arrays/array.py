import numpy as np 
# Create an empty array 
empa = np.empty((3, 4), dtype=int) 
print("Empty Array") 
print(empa) 
# Create a full array 
flla = np.full([3, 3], 55, dtype=int) 
print("\nFull Array") 
print(flla) 
a = np.zeros(3, dtype=int) 
print("Matrix a : \n", a) 
b = np.zeros([3, 3], dtype=int) 
print("\nMatrix b : \n", b) 
c = np.zeros([5, 3]) 
print("\nMatrix c : \n", c) 
d = np.zeros([5, 2], dtype=float) 
print("\nMatrix d : \n", d) 
array = np.ones(5) 
print(array) 
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10], 
                [11, 12, 13, 14, 15], 
                [16, 17, 18, 19, 20] 
                ])  
# View array 
print(arr) 
# Check for some lists 
print([1, 2, 3, 4, 5] in arr.tolist()) 
print([16, 17, 20, 19, 18] in arr.tolist()) 
print([3, 2, 5, -4, 5] in arr.tolist()) 
print([11, 12, 13, 14, 15] in arr.tolist()) 