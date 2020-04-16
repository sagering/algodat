
class UnionFind:
	def __init__(self, n):
		self.roots = [i for i in range(n)]
		self.sizes = [1] * n
		
	def find(self, i):
		while True:
			ri = self.roots[i]
			if ri == i: break
			i = ri
			
		return ri
		
	def union(self, i, j):
		ri = self.find(i)
		rj = self.find(j)
		
		# Choose node with smallest index as new root.
		if ri < rj:
			self.__adjust_roots(j, ri)
			self.sizes[ri] += self.sizes[rj]
		elif rj < ri:
			self.__adjust_roots(i, rj)
			self.sizes[rj] += self.sizes[ri]

	def __adjust_roots(self, i, r):
		while True:
			ri = self.roots[i]
			if ri == r: break
				
			self.roots[i] = r
			i = ri
