class FileReader():

	def __init__(self, path = None):
		self.file_path = path

	def read(self):
		try:
			with open(self.file_path, 'r') as file:
				return file.read()
		except FileNotFoundError:
			return ''