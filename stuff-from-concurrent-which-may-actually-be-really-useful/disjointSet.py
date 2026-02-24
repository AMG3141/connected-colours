'''
Disjoint set connected components algorithm from concurrent lectures
'''

'''
Random notes while i'm trying to remember what this thing actually is:
- parent and rank are integer arrays containing the parent of a given node and the rank of a given node (what is rank again? is it the node id, so it is correct to say "parent of a given rank"??)
- no, i think rank is the component each node is part of (the nodes are simply indexed by the array indices)

algorithm (roughly):
- initialise each node to its own component
- do a relax on each edge (a "relax" is just the operation that is performed when visiting an edge). in this case we do a union of the src and dest nodes (i.e. put them in the same set)
- that's pretty much it. just a bit of tidying up of the labels (basically just restrict them to a narrow domain)
- can also calculate the sizes of the components (may be useful i guess)

things i need to do:
- get a graph representation. with images it might be difficult? is there much to be done with sparse representations? because it is so regular i definitely think there is some sort of efficiency to be had
- write the below functions. can probably just copy what i did in concurrent. also get rank and parent arrays
- parallelising shouldn't be too difficult, as you just parallelise the relax stage by number of edges (though not sure how many cpus microcontrollers tend to have)
- the updating of rank and parent i guess would be the most difficult things to parallelise

actually thinking about it i'm not sure if this algorithm is worth it for images. i think it will basically just boil down to looking at the 8-way connectivity of each pixel

i think give it a go anyway. the other file can generate an adjaency matrix. basically just check if the pixel values match and it should give the connected componenets...
'''

def makeSet(e):
	return # position storing e in this set... whatever that means

def union(A, B):
	# return set of elements in either A or B naming the result A or B
	pass

def find(e):
	# return the set conatining the element e
