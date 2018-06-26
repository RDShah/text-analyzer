import statistics
from reader import clean_read

def ensure(obj, stat):
	if type(obj) is not tuple:
		assert type(obj) in [list, str], 'Data format of object is unrecognized.  Pass in string, list of words, or output of '+ stat +' statistic.'
		if type(obj) == str and len(obj)>4 and obj[-4:]=='.txt': obj = clean_read(obj)
		return getattr(statistics,stat)(obj)
	assert obj[0] == stat, 'Data format of object is unrecognized.  Pass in string, list of words, or output of '+ stat +' statistic.'
	return obj