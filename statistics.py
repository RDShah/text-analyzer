'''
input: list of words or raw string
output: dictionary mapping words to frequencies
'''
def word_frequency(text):
	if type(text) == str:
		text = text.split(' ')
	d = dict()
	for word in set(text):
		d[word] = 0
	for word in text:
		d[word] += 1
	return 'word_frequency',d

'''
input: list of words or raw string
output: dictionary mapping lengths of words to frequencies
'''
def word_length_frequency(text):
	if type(text) == str:
		text = text.split(' ')
	d = dict()
	for word in set(text):
		d[len(word)] = 0
	for word in text:
		d[len(word)] += 1
	return 'word_length_frequency',d

def average_word_length(text):
	if type(text) == str:
		text = text.split(' ')
	return 'average_word_length',len(''.join(text))/len(text)