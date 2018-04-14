import calculator

print("This is a calculator application.")

while True:
	print("Please choose the operation wanted by entering one of the following:")
	print("'Add' for Add,  'Sub' for Subtract, ")
	print("'Mul' for Multiply,  'Div' for Divide.")
	operation = int(input("Please type the operation you would like: "))
	first_number = int(input("Please enter the first number: "))
	second_number = int(input("Please enter the second number: "))
	

	if operation == "Add":
		print(calculator.add(first_number, second_number))
	elif operation == "Sub":
		print(calculator.subtract(first_number, second_number))
	elif operation == "Mul":
		print(calculator.multiply(first_number, second_number))
	elif operation == "Div":
		print(calculator.divide(first_number, second_number))
