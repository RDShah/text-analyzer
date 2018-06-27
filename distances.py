import numpy as np
from statistics import *
from typecheck import ensure
'''
input: word frequency statistic
output: sum_{shared word} |rank1(word)-rank2(word)|*weight(word)
'''
def weighted_rank_difference(d1,d2):
	d1 = ensure(d1,'word_frequency')[1]
	d2 = ensure(d2,'word_frequency')[1]

	n1 = sum(d1.values())
	n2 = sum(d2.values())

	ordered_words1 = list(d1)
	ordered_words1.sort(key = lambda word: -d1[word])
	ordered_words2 = list(d2)
	ordered_words2.sort(key = lambda word: -d2[word])

	# print(ordered_words2[:10])

	rank1 = dict()
	rank2 = dict()
	j = 0
	for i in range(len(ordered_words1)):
		rank1[ordered_words1[i]] = j
		if i < len(ordered_words1)-1 and d1[ordered_words1[i+1]] < d1[ordered_words1[i]]:
			j+=1
	j = 0
	for i in range(len(ordered_words2)):
		rank2[ordered_words2[i]] = j
		if i < len(ordered_words2)-1 and d2[ordered_words2[i+1]] < d2[ordered_words2[i]]:
			j+=1

	weight = dict()
	Z = 0
	for word in set(d1).intersection(set(d2)):
		weight[word] = - d1[word]/n1 * (np.log(d1[word])-np.log(n1)) - d2[word]/n2 * (np.log(d2[word])-np.log(n2))
		Z += weight[word]
	return sum(abs(rank1[word]-rank2[word])*weight[word] for word in weight)/Z

'''
input: word frequency statistic
ignores non-mutually-present words
output: sum p log(p/q)
'''
def kl_divergence(d1,d2):
	d1 = ensure(d1,'word_frequency')[1]
	d2 = ensure(d2,'word_frequency')[1]

	intersection = set(d1).intersection(set(d2))

	n1 = sum(d1[x] for x in intersection)
	n2 = sum(d2[x] for x in intersection)

	const = np.log(n2)-np.log(n1)

	return sum(d1[word]/n1 * (np.log(d1[word]) - np.log(d2[word]) + const) for word in intersection)


'''
input: word frequency statisitc, or set of words used, or list of words
output: |intersection|/|union|
'''
def vocab_overlap(d1,d2):
	d1 = set(d1)
	d2 = set(d2)
	return len(d1.intersection(d2))/len(d1.union(d2))
