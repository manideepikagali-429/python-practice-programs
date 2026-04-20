def multipleReturn(myList): 
    maxValue=max(myList) 
    total=sum(myList) 
    return maxValue,total 
num=int(input('Enter no.of elements')) 
numList=list()
for i in range (0,num): 
    numList.append(int(input('Enter the number'))) 
maximum,total=multipleReturn(numList) 
print('Maximum = ',maximum) 
print('Total = ',total)