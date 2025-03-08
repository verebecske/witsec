# main.py
def next_collatz_number(number: int):
	if number % 2 == 0:
		number = int(number / 2)
	else:
		number = 3 * number + 1
	return number

def count_steps(number: int):
	steps = 0
	while number != 1:
		print(number, end="->")
		steps += 1
		number = next_collatz_number(number)	
	print(number)
	print(f"steps: {steps}")
	return steps

def main():
	max_number = 0
	max_steps = 0
	for i in range(1, 101):
		steps = count_steps(i)
		if max_steps < steps:
			max_steps = steps
			max_number = i
	print(f"Max steps: {max_steps} number: {max_number}")

main()