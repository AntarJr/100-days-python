import os 
logo = """
                         ___________
                                  /
                          )_______(

                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
"""
np_dic={
  
}
highest = 0
winner = ""
while True :
    name = input("What is your Name ?\n").lower().strip()
    price = int(input("What is your Bidding price ? : \n$"))
    np_dic[name] = price 
    if price > highest :
        highest = price
    
    choice = input("Are there any other bidders? Type 'yes or 'no' \n").lower().strip()
    if choice != "yes" and choice != "no" :
        print("Please Choose either yes or no ")
        continue
    elif choice == "yes" :
        os.system("cls")
        continue
    elif choice == "no" :
        break
    else :
        break
for bidder in np_dic:
        if np_dic[bidder] == highest :
            winner = bidder

print(f"the winner is {winner} with a bid of ${highest}")