import numpy as np
import matplotlib.pyplot as plt
from distances import *
import lyricscorpora as lc


fn1 = 'warandpeace1.txt'
fn2 = 'warandpeace2.txt'
fn3 = 'feynman.txt'

# strings = [-1]*3

# strings[0] = 'test_documents/'+fn1
# strings[1] = 'test_documents/'+fn2
# strings[2] = 'test_documents/'+fn3

fns = []

for artist in ['Kanye West','Kendrick Lamar','J Cole','Logic']:
	for album in lc.Artist(artist).get_album_list():
		fns.append('test_documents/'+artist+' - '+album.name+'.txt')

def pairwise_distances(files):
	half = np.zeros((len(files),len(files)))
	for i in range(1,len(files)):
		for j in range(i):
			half[i][j] = weighted_rank_difference(files[i],files[j])
			if np.isnan(half[i][j]):
				half[i][j]=0
	return half+half.T

def mds(D):
	n = D.shape[0]
	H = np.eye(n)-np.ones((n,n))/n
	B = -0.5*H.dot(np.multiply(D,D)).dot(H)
	lambdas,v = np.linalg.eig(B)
	# print(lambdas)
	# print(v)
	# print(v[:,:2].shape)
	# quit()
	return v[:,:2].dot(np.sqrt(np.diag(lambdas[:2])))

real_D = pairwise_distances(fns)
print(real_D)
# plt.matshow(real_D)
# plt.show()
points = mds(real_D)

# a = np.zeros((3,3))
# for i in range(1,3):
# 	for j in range(i):
# 		a[i][j] = np.linalg.norm(points[i]-points[j])
# fake_D = a+a.T

plt.scatter(points[:,0],points[:,1],c=['blue']*9+['red']*7+['green']*8+['yellow']*7)
plt.axes().set_aspect('equal')
plt.show()