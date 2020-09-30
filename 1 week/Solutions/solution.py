import sys 

def discriminant(a, b, c):
	return b**2 - 4*a*c

def first_root(a, b ,c):
	return (-b - discriminant(a, b, c)**0.5)/(2*a)

def second_root(a, b, c):
	return (-b + discriminant(a, b, c)**0.5)/(2*a)

if __name__ == '__main__':

	a = int(sys.argv[1]) 
	b = int(sys.argv[2]) 
	c = int(sys.argv[3])

	print (int(first_root(a, b, c)))
	print (int(second_root(a, b, c)))

