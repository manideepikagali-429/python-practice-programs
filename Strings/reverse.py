filename=input('enter filename')
f=open(filename,'r')
for line in reversed(list(f)):
    print(line[::-1],end='')
f.close()