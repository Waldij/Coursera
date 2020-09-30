import sys

if __name__ == '__main__':
	
	stair_block = "#"
	air_block = " "

	stair_length = int(sys.argv[1])

	for i in range(1, stair_length + 1):
		print(air_block * (stair_length - i) + stair_block * i)