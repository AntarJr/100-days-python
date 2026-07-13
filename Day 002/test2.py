print("Welcome to the Life stats Program")
name= input("What is your name \n")
age= input("How old are you \n")
country = input("what country do you live in \n")
Dream_job= input("what is your dream job \n")
Hours_of_study= int(input("How many hours do you study per day? \n"))
Hours_per_week= Hours_of_study * 7
Months_of_python= int(input("How many months have you been learning Python? \n"))
Hours_passed= (Months_of_python * 4 ) * Hours_per_week
Year_Hours = Hours_of_study * 365

print(f"hello {name} ! \n")

print(f"your are {age} years old.")
print(f"you live in {country}.")
print(f"your dream job is to become a {Dream_job}.")
print(f"if you study {Hours_of_study} Hours each day, you are studying {Hours_per_week} Hours each week \nwhich means you are investing in your future")
print(f"you have already studied {Hours_passed} Hours of python")
print(f"In one year,\nYou will approximatly have {Year_Hours} Hours of study under your belt")
print(f"Good luck, {name} !")