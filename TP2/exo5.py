#Exercice 5 


x = int(input("Chiffre"))
if x == 0:
    print(x ,"est nul (est postif)" )
else :
    if x>0 and x%2 == 0:
        print(x , "est postive est pair")
    else :
        if x>0 and x%2 != 0:
            print(x , "est postive est impair")
        else :
            if x<0 and x%2 == 0:
                print(x , "est negatif est pair")
            else:
                print(x , "est negatif est impair")


 
