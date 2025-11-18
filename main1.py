number1 = float(input("Веддіть число "))
action = input("Веддіть дію ")
number2 = float(input("Веддіть число "))

result = None

if action == "+":
	result = number1 + number2
elif action == "-":
	result = number1 - number2
elif action == "*":
	result = number1 * number2
elif action == "/":
	if number2 == 0:
		print("На нуль ділити не можливо")
	else:
		result = number1 / number2
else:
	print("Такої дії не існує")

print("Результат дії: \n", result)