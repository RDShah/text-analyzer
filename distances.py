import numpy as np
'''
input: word frequency statistic
output: sum_{shared word} |rank1(word)-rank2(word)|*weight(word)
'''
def weighted_rank_difference(d1,d2):
	n1 = sum(d1.values())
	n2 = sum(d2.values())

	ordered_words1 = list(d1.keys())
	ordered_words1.sort(key = lambda word: -d1[word])
	ordered_words2 = list(d2.keys())
	ordered_words2.sort(key = lambda word: -d2[word])

	rank1 = dict()
	rank2 = dict()
	for i in range(len(ordered_words1)):rank1[ordered_words1[i]] = i
	for i in range(len(ordered_words2)):rank2[ordered_words2[i]] = i

	weight = dict()
	Z = 0
	for word in set(ordered_words1).intersection(set(ordered_words2)):
		weight[word] = - d1[word]/n1 * (np.log(d1[word])-np.log(n1)) - d2[word]/n2 * (np.log(d2[word])-np.log(n2))
		Z += weight[word]
	for word in weight.keys():
		weight[word] /= Z

	return sum(abs(rank1[word]-rank2[word])*weight[word] for word in weight.keys())