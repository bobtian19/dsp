# Matrix Algebra

##Linear Algebra Worksheet
import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.matrix('6 2 -3 5')
v = np.matrix('3 5 -1 4')
w = np.matrix('1; 8; 0; 5')
a = 6

#Matrix dimensions
print A.shape # A: 2x3
print B.shape # B: 2x2
print C.shape # C: 3x2
print D.shape # D: 2x3
print u.shape # u: 1x4
print v.shape # v: 1x4
print w.shape # w: 4x1

#Vector Operations
print u+v # [[ 9  7 -4  9]]
print u-v # [[ 3 -3 -2  1]]
print a*u # [[ 36  12 -18  30]]
print np.inner(u,v) # 51
print np.asscalar(np.inner(u,u))**0.5 # 8.60232526704

#Matrix Operations
# A+C not defined (can't add if they're not the same dimensions)
print A - np.transpose(C) # [[-4 -7 -3],[ 3  6  4]]
print np.transpose(C) + 3*D # [[14  3  3],[ 2  7  9]]
print B*A #[[-1 -5 -1],[ 2  7  4]]
# BA^T not defined (B is 2x2, A^T is 3x2. The inner dimensions do not match)
# BC not defined (B is 2x2, C is 3x2. The inner dimensions do not match)
print C*B #[[ 5 -6],[ 9 -8],[ 6 -6]]
print B**4 #[[ 1 -4],[ 0  1]]
print A*np.transpose(A) #[[14 28],[28 69]]
print D*np.transpose(D) #[[14 -4],[-4 14]]
