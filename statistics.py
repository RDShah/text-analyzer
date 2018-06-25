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