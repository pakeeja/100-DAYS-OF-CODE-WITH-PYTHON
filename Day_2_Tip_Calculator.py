#This is tip calcultor

print("Welcome to the tip calculator .")
bill=input("What was the total bill ? $")
percent_tip=input("What percentage of tip would you like to give? 10 ,12 or 15? ")
people=input("How many people to split the bill ? ")
tip=(float(bill)/int(people))*(int(percent_tip)/100)
print(f"Each person should pay : ${round(tip+float(bill)/int(people),2)}")