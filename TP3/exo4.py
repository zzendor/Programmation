mode=int(input("0 = for ; 1 = While"))
Nb=int(input("NOMBRE"))
a=1
y=1
if mode == 0:
    for i in range(1, Nb+1):
        a=a*i
        print(a)
    
else:
    while y!= Nb+1:
        a=a*y
        y+=1
        print(a)
    


