characters_to_keep = set('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ')

def clean_read_all(ss):
	return [clean_read(s) for s in ss]

def file_to_string(file):
	return ''.join([line for line in file])

def clean_string(s):
	return ''.join([letter for letter in s if letter in characters_to_keep]).lower()

def clean_read(s):
	with open(s) as file:
		return clean_string(file_to_string(file))
