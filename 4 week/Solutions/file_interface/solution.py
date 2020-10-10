import tempfile
import os.path

class File():
	"""docstring for ClassName"""

	def __init__(self, path_to_file):
		self.path_to_file = path_to_file
		if not os.path.exists(self.path_to_file):
			with open(self.path_to_file, 'w'):
				pass

	def read(self):
		with open(self.path_to_file, 'r') as file:
			return file.read()

	def write(self, string_to_write):
		with open(self.path_to_file, 'w') as file:
			file.write(string_to_write)

	def write_next_line(self, string_to_write):
		with open(self.path_to_file, 'a') as file:
			file.write(string_to_write)

	def __add__(self, *args):

		files_content = []
		files_content.append(self.read())
		for obj in args:
			files_content.append(obj.read())

		with tempfile.NamedTemporaryFile(delete = False) as temp:
			new_file = File(temp.name)

			for content in files_content:
				new_file.write_next_line(content)

		return new_file 

	def __str__(self):
		return self.path_to_file

	def __getitem__(self, index):
		with open(self.path_to_file, 'r') as file:
			lines = list(file)
			return lines[index]