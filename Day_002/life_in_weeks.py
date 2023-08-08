# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

years_remain = 90 - int(age)
months_remain = years_remain * 12
weeks_remain = years_remain * 52
days_remain = years_remain * 365

print(f"You have {days_remain} days, {weeks_remain} weeks, and {months_remain} months left.")
