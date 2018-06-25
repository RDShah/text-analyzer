from reader import clean_read
from statistics import *
from distances import *

fn1 = 'warandpeace1.txt'
fn2 = 'warandpeace2.txt'
fn3 = 'feynman.txt'

# fn1 = 'ex1.txt'
# fn2 = 'ex2.txt'
# fn3 = 'ex3.txt'

string1 = clean_read('test_documents/'+fn1).split(' ')
string1_again = clean_read('test_documents/'+fn1).split(' ')
string2 = clean_read('test_documents/'+fn2).split(' ')
string3 = clean_read('test_documents/'+fn3).split(' ')

# print('stirng',string1==string1_again,string1[:10])

#print(string2[:10])
#quit()

d1 = word_frequency(string1)
d1_again = word_frequency(string1)
d2 = word_frequency(string2)
d3 = word_frequency(string3)

#print('stat',d1==d1_again,d1['and'],d1['the'],d1['rely'],d1['least'],d1['something'],d1['us'],d1['expression'])

# x = weighted_rank_difference(d1,d2)
# y = weighted_rank_difference(d1,d2)
# print('result',y==x,x)

print('Distance between 1 and 2:',weighted_rank_difference(d1,d2))
print('Distance between 2 and 3:',weighted_rank_difference(d2,d3))
print('Distance between 1 and 3:',weighted_rank_difference(d1,d3))