
#A tip calculator to calculate tips. Code could have been much cleaner but this was written for learning purposes to make it as readable as possible.
#By: Mohammed Salim Dason
#Email: dasonsalim@outlook.com
#Github: salimdason
#Website: coming soon.


print("Welcome to the tip calculator")
total_bill = input("How much was the total bill? ")
total_bill_conv = float(total_bill)
tip = input("What percentage of tip would you like to give? ")
tip_conv = int(tip)
people_to_split = input("How many people would be splitting the bill? ")
people_to_split_conv = int(people_to_split)
#Calculations
tip_percentage = tip_conv * 100 / 100
total_to_pay = total_bill_conv + tip_percentage
split_amount = total_to_pay / people_to_split_conv
result = round(split_amount, 2)
print(f"Each person has to pay {result} USD in total")