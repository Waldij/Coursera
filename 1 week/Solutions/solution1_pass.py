import sys

if __name__ == '__main__':
	
	digit_string = sys.argv[1]
	sum_of_digits = 0

	for digit in digit_string:
		sum_of_digits += int(digit)

	print (sum_of_digits)