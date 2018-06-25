'''
input: list of words
output: dictionary mapping words to frequencies
'''
def word_frequency(text):
	d = dict()
	for word in set(text):
		d[word] = 0
	for word in text:
		d[word] += 1
	return d

'''
input: list of words
output: dictionary mapping lengths of words to frequencies
'''
def word_length_frequency(text):
	d = dict()
	for word in set(text):
		d[len(word)] = 0
	for word in text:
		d[len(word)] += 1
	return d

def average_word_length(text):
	return len(''.join(text))/len(text)