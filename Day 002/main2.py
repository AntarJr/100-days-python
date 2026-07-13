print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people=int(input("How many people to split the bill?"))
bill_tip=bill*(tip/100)
final_bill=bill+bill_tip
Bill_per_person=final_bill/people
Final_person_bill=round(Bill_per_person, 2)
print(f"Each person should pay: ${Final_person_bill}")