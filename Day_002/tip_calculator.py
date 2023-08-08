# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator.")
bill_tot = float(input("What was the total bill? "))
tip_pct = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
ppl_tot = int(input("How many people to split the bill? "))

each_tot = (bill_tot + (bill_tot * tip_pct / 100)) / ppl_tot
# each_tot = round(each_tot, 2)
fnl_amt = "{:.2f}".format(each_tot)

# print(f"Each person should pay: {each_tot}")
print(f"Each person should pay: {fnl_amt}")
