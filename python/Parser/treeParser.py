
from pathlib import Path
tree = {'a': ['b', 'c'],
		'b': ['d', 'e'],
		'c': [],
		'd': ['f'],
		'e': [],
		'f': []}

class treeNode(object):
	pass

class treeParser(object):
	"""Parsing a complex dict stucture 
	:param tree: The tree to parse ...
	:type tree : a dict wich can be walked
	:param filePath: The orginal file loction
	"""
	def __init__(self, filePath: Path, tree: dict):
		self.filePath

	sub = []
	def walk(self):
		""" walk the tree"""
		genericStart()
		for object in sub:
			try:
				object.start()
			except:
				Print(f"error in object.start on {sys._getframe().f_back.f_lineno}")


	def genericStart(self):
		for frame in df['master']:
			print(frame)


	def children(token, tree):
		"returns a list of every child"
		child_list = []
		to_crawl = deque([token])
		while to_crawl:
			current = to_crawl.popleft()
			child_list.append(current)
			node_children = tree[current]
			to_crawl.extend(node_children)
		return child_list

