import numpy as np
import matplotlib.pyplot as plt
from distances import *


fn1 = 'warandpeace1.txt'
fn2 = 'warandpeace2.txt'
fn3 = 'feynman.txt'

strings = [-1]*3

strings[0] = 'test_documents/'+fn1
strings[1] = 'test_documents/'+fn2
strings[2] = 'test_documents/'+fn3

def pairwise_distances(files):
	half = np.zeros((len(files),len(files)))
	for i in range(1,len(files)):
		for j in range(i):
			half[i][j] = weighted_rank_difference(files[i],files[j])
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

real_D = pairwise_distances(strings)
points = mds(real_D)

a = np.zeros((3,3))
for i in range(1,3):
	for j in range(i):
		a[i][j] = np.linalg.norm(points[i]-points[j])
fake_D = a+a.T

print(real_D-fake_D)

plt.scatter(points[:,0],points[:,1])
plt.axes().set_aspect('equal')
plt.show()