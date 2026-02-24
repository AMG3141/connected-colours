'''
Generate an adjancey matrix for an image (i.e. a rectangular graph in which each corner node is connected to its 3 neighbours, each non-corner edge node is connected to its 5 neighbours, and each interior node is connected to its 8 neighbours)
'''

import numpy as np
import matplotlib.pyplot as plt

imRows = 16
imCols = 16

def coordsToNodeId(row, col):
	'''Assuming top-left pixel has ID 0 and they increase left to right, top to bottom'''
	return row * imCols + col

def setNeighbours(row, col, adjMat):
	'''AN EDGE SHOULD ONLY BE MADE IF THE PIXELS ARE SIMILAR COLOURS!!! Now this raises the question of if we even want do to it this way. Jumping around memory like this is less efficient that just proceeding linearly, but will probably give a less good algorithm'''
	# Basic approach (to make the adjacency matrix for the whole image)
	targetId = coordsToNodeId(row, col)
	for i in range(row - 1, row + 2):
		for j in range(col - 1, col + 2):
			if i < 0 or j < 0 or i >= imRows or j >= imCols or (i == row and j == col): continue
			otherId = coordsToNodeId(i, j)
			mat[otherId, targetId] = 1

	# Connected components approach (only draw an edge if the two pixels have the same colour) !!! REQUIES AN IMAGE DUH
	# for undirected graphs only need to consider the top half of the matrix
	
mat = np.zeros([imRows * imCols, imRows * imCols]) # Indexed by: [dest, source] (that is the convention adopted by Hans so I'm sticking with it. Technically doesn't matter for this since it's undirected but eh)
for i in range(imRows):
	for j in range(imCols):
		setNeighbours(i, j, mat)

plt.imshow(mat)
plt.show()

outstr = ""
for i in range(imRows * imRows):
	for j in range(imCols * imCols):
		outstr += f"{mat[i, j]} "
	outstr += '\n'
print(outstr)
