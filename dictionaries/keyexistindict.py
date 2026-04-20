string=input('Enter a string') 
char_dict=dict() #{} 
for letter in string: 
    #char_dict[letter]=string.count(letter) 
    if(letter in char_dict): 
        char_dict[letter]+=1 
    else: 
        char_dict[letter]=1 
print(char_dict)