import random
while True:
    print("Guess the number Game !!!")
    a=random.randint(1,100)
    t=0
    while True:
        t+=1
        b=int(input("Your guess:"))
        if t==10:
            print("You loss")
        elif a>b:
            print ("higer than",b)
        elif a<b:
            print("less than",b)
        elif a==b:
            print("your guess is correct!!!")
            if t==1:
                print("Must be your luck found it in one try")
            elif t>5:
                print("you tried quiet a lot of trys itseems")
            break
    q=input("Do u wanna try again!!(Yy/Nn)")
    if q == "n" or q=="N":
        break
print("Thank you for playing my game:)")


        
