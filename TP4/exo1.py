results = []
number= float(input("valeur:"))
for i in range(1, 11):
    result = number * i
    results.append(result)
    print(number ,'*' ,i,'=' ,round(results[i-1],1))



