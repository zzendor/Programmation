test1 = True and (True or False)
test2 = False

if test1 :
    print("Ré", end=" ")

if (test1 or test2) :
    if not test1 :
        print("Do", end=" ")
    else :
        print("Fa", end=" ")
else :
    print("Mi", end=" ")

print("Si")


    

