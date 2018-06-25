from reader import clean_read
from statistics import *
from distances import *

fn1 = 'ex1.txt'
fn2 = 'ex2.txt'
fn3 = 'ex3.txt'

string1 = clean_read('test_documents/'+fn1)
string2 = clean_read('test_documents/'+fn2)
string3 = clean_read('test_documents/'+fn3)

d1 = word_frequency(string1)
d2 = word_frequency(string2)
d3 = word_frequency(string3)

print('Distance between 1 and 2:',weighted_rank_difference(d1,d2))
print('Distance between 1 and 3:',weighted_rank_difference(d1,d3))
print('Distance between 2 and 3:',weighted_rank_difference(d2,d3))