import Parser
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
		self.filePath = filePath

	sub = []
	def walk(self):
		""" walk the tree with subscriders"""
		self.genericStart()
		for object in self.sub:
			try:
				object.start()
			except:
				Print(f"error in object.start on {sys._getframe().f_back.f_lineno}")


	def genericStart(self):
		frame = Parser.db['Master']
		erro = True
		for idx , val in frame.iterrows():
			if val.Mode != "FileRegex":
				continue
			erro = False
			try:
				print(val.eval)
				eval(val.eval)
			except:
				pass				
			print(self)
			print(val)
		if erro:
				print("Error did not find a single FileRegex in Master" )


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

