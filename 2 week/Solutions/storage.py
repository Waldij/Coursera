import argparse
import os
import tempfile
import json

#Pars part
parser = argparse.ArgumentParser(description='Key-Values')
parser.add_argument('--key', type = str, help='Key')
parser.add_argument('--val', type = str, help='Value to store')
args = parser.parse_args()

current_dict = dict()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#print(storage_path)

if os.path.exists(storage_path):
	#print("Файл существует")
	if os.stat(storage_path).st_size > 0:
		#print("Файл непустой")
		with open(storage_path, 'r', encoding="utf-8") as f:
			current_dict = json.load(f)
else:
	with open(storage_path, 'w') as f:
		pass
#Testing
if args.val == None:
	with open(storage_path, 'r') as f:
		if args.key in current_dict:
			#print ("Value by key")
			print(', '.join(current_dict[args.key])) 
			#print (current_dict[args.key])
		else:
			pass
			#print ("Такого ключа нет")
else:
	with open(storage_path, 'w') as f:
		if args.key not in current_dict:
			data_to_store = dict()
			values_list = list()
			values_list.append(args.val)
			data_to_store[args.key] = values_list
			#print ("Data to store")
			#print (data_to_store)
			current_dict.update(data_to_store)
			json.dump(current_dict, f)
		else:
			#print("Такая пара уже существует")
			values_list = list(current_dict[args.key])
			values_list.append(args.val)
			current_dict[args.key] = values_list
			json.dump(current_dict, f)



