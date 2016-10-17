#
#                                                                        
# Title: tutorial.py                                                 
# Author: Trond Skogland (trond.skogland@atea.no)                        
#                                                                        
# Description:                                                             
# Made as part of the youtube tutorial                                                                       
#

# 1. This program returns the sum of num1 and num2

def add (num1, num2):
	return num1 + num2

def sub (num1, num2):
	return num1 - num2

def multi (num1, num2):
	return num1 * num2

def div (num1, num2):
	return num1 / num2


def main ():
	operation = input("What do you want to do (+,-,*,/): ")
	print(operation)
	if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		# Invalid operator
		print("You must enter a valid operator")
	else:
		var1 = int(input ("Enter num1: "))
		var2 = int(input ("Enter num2: "))
		if (operation == '+'):
			print(add(var1, var2))
		elif (operation == '-'):
			print(sub(var1, var2))
		elif (operation == '*'):
			print(multi(var1,var2))		
		else:
			print(div(var1,var2))

main()
