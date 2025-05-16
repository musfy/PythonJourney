#Write a program to prompt the user for hours and rate per hour to
#compute gross pay

rate = input("Enter your rate")
hours = input("Enter your hours")

pay = float(rate) * float(hours)

print("Your pay is",pay)