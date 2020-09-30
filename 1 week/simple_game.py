import random 

hidden_number = random.randint(0,101)

while(True):
	players_answer = input("Введите число: ")

	if not players_answer or players_answer == "exit":
		break

	if not players_answer.isdigit():
		print("Введите правильное число!")
		continue

	players_answer = int(players_answer)

	if (players_answer > hidden_number):
		print("Загаданное чило меньше")
	elif (players_answer < hidden_number):
		print("Загаданное чило больше")
	else:
		print("Вы угадали!")
		break


