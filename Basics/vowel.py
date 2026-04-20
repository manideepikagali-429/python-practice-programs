String = input('Enter a string') 
vowels = [String.count(x) for x in "aeiou"] 
print('Occurences of vowels aeiou: ', vowels) 
print('The numbers vowels in this ', String ,' are: ',sum(vowels))