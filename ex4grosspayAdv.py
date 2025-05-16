#Write a program to prompt the user for hours and rate per hour to
#compute gross pay

rate = input("Enter your rate\n")
hours = input("Enter your hours\n")

if float(hours) > 40:

	pay = float(rate) * 40
	overTime = float(hours) - 40
	
	overTimePay = overTime * float(rate) * 1.5
	pay = pay + overTimePay
	print("Your pay is", pay)
else:
	pay = float(rate) * float(hours)
	print("Your pay is", pay)