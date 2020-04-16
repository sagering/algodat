def find_bridges(graph):
	n = len(graph)
	lowlink = [0] * n
	ts = [0] * n
	t = 0

	visited = set()
	bridges = []

	def rec(i, p):
		nonlocal t

		ts[i] = t
		lowlink[i] = t
		visited.add(i)

		t += 1

		for j in range(n):
			if graph[i][j] == 1:
				if j == p: continue
				if j == i: continue
				if j not in visited:
					rec(j, i)
					# Propagate the lowlink value.
					lowlink[i] = min(lowlink[i], lowlink[j])
				else:
					# Set the lowlink value.
					lowlink[i] = min(lowlink[i], its[j])
					
				# If lowlink of j is larger than the current node i's t,
				# then there was no path back from node j to node i.
				# Hence node j constitutes the start of a new strongly connected component.
				if lowlink[j] > ts[i]:
					bridges.append((i, j))

	for i in range(n):
		if i not in visited:
			rec(i, -1)

	return bridges
	
def find_articulation_points(graph):
	n = len(graph)
	lowlink = [0] * n
	ts = [0] * n
	t = 0

	visited = set()
	points = set()

	def rec(i, p):
		nonlocal t

		ts[i] = t
		lowlink[i] = t
		visited.add(i)

		t += 1
		cnt = 0 # count of unvisited child nodes

		for j in range(n):
			if graph[i][j] == 1:
				if j == p: continue
				if j == i: continue
				if j not in visited:
					rec(j, i)
					# Propagate the lowlink value.
					lowlink[i] = min(lowlink[i], lowlink[j])
				else:
					# Set the lowlink value.
					lowlink[i] = min(lowlink[i], ts[j])
					cnt += 1
				
				# Node is an articulation point:
				# If it is part of a bridge,
				if lowlink[j] > ts[i]:
					points.add(i)
				# or it is not a starting node and
				# it is the entry point to a cycle,
				elif p != -1 and lowlink[j] == ts[i]:
					points.add(i)
				# or if it is a starting node and
				# it has two or more unvisited children
				elif p == -1 and cnt > 1:
					points.add(i)

	for i in range(n):
		if i not in visited:
			rec(i, -1)

	return points
	
def find_connected_components(graph):
	n = len(graph)
	ts = [0] * n
	t = 1

	visited = set()
	
	def rec(i):
		nonlocal t
		
		visited.add(i)
		ts[i] = t
		
		for j in range(n):
			if graph[i][j] == 1 and j not in visited:
				rec(j)
		
	for i in range(n):
		if i not in visited:
			rec(i)
			t += 1

	ccs = {}
	for i in range(n):
		if ts[i] not in ccs:
			ccs[ts[i]] = []
			
		ccs[ts[i]].append(i)
		
	return [v for v in ccs.values()]
