import calculator

print("This is a calculator application.")

while True:
	print("Please choose the operation wanted by entering one of the following:")
	print("'Add' for Add,  'Sub' for Subtract, ")
	print("'Mul' for Multiply,  'Div' for Divide.")
	print("Type 'quit' to exit")
	operation = input("Please type the operation you would like: ")
	if operation == "quit":
		break
	first_number = int(input("Please enter the first number: "))
	second_number = int(input("Please enter the second number: "))
	

	if operation == "Add":
		print("result is", calculator.add(first_number, second_number))
	elif operation == "Sub":
		print("result is", calculator.subtract(first_number, second_number))
	elif operation == "Mul":
		print("result is", calculator.multiply(first_number, second_number))
	elif operation == "Div":
		print("result is", calculator.divide(first_number, second_number))
