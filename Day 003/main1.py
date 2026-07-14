print("welcome to python pizza deliveries!")
size = input("what size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

if size == "s" :
    bill = 15
    if pepperoni == "y":
        bill += 2
    if extra_cheese == "y" :
        bill +=1
        print(f"Your bill is ${bill}.")
    else :
        print(f"your bill is ${bill}")


elif size == "m" :
    bill = 20
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y" :
        bill +=1
        print(f"Your bill is ${bill}.")
    else :
        print(f"your bill is ${bill}")


else  :
    bill = 25
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y" :
        bill +=1
        print(f"Your bill is ${bill}.")
    else :
        print(f"your bill is ${bill}")
