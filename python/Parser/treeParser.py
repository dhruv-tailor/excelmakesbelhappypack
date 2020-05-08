import Parser, sys
from singledispatchmethod import singledispatchmethod
from typing import List
from pathlib import Path

tree = {'a': ['b', 'c'],
		'b': ['d', 'e'],
		'c': [],
		'd': ['f'],
		'e': [],
		'f': []}

class visitor(object):
	def do(self, obj):
		print(obj,end=" ")
		return obj
	@singledispatchmethod
	def visitStart(self, arg):
		raise NotImplementedError(f"Cannot handle {type(arg)}")
	@visitStart.register
	def _(self, arg: int):
		return self.do( str(arg))
	@visitStart.register
	def _(self, arg: str):
		return self.do(str(arg))
	@visitStart.register
	def _(self, arg: dict):
		return self.do(str(arg)	)
	@visitStart.register
	def _(self, arg: float):
		return self.do(str(arg)	)
	@visitStart.register
	def _(self, arg: list):
		return self.do(str(arg)	)
	@singledispatchmethod
	def visitEnd(self, arg):
		raise NotImplementedError(f"Cannot handle {type(arg)}")
	@visitEnd.register
	def _(self, arg: int):
		pass
	@visitEnd.register
	def _(self, arg: str):
		pass
	@visitEnd.register
	def _(self, arg: dict):
		pass
	@visitEnd.register
	def _(self, arg: list):
		pass
	@visitEnd.register
	def _(self, arg: float):
		pass

class dictVisitor(visitor):
	lastKey = []
	depth = 0
	@singledispatchmethod
	def visitStart(self, arg):
		return  super().visitStart(arg)
	@singledispatchmethod
	def visitEnd(self, arg):
		return  super().visitEnd(arg)
	@visitStart.register
	def _(self, arg :dict):
		self.depth = self.depth + 1
		self.do("{\n".ljust(self.depth + 2,"\t"))
		for key, value in arg.items():
			self.lastKey.append(key)
			self.visitStart(key)
			self.visitEnd(key)
			self.do("= ")
			self.visitStart(value)
			self.visitEnd(value)
			self.lastKey.pop()
			self.do("\n".ljust(self.depth + 1,"\t"))
	@visitEnd.register
	def _(self, arg :dict):
		self.depth = self.depth - 1
		self.do("}".ljust(self.depth,"\t"))
	@visitStart.register
	def _(self, arg :list):
		self.visitStart(arg[0])
		self.visitEnd(arg[0])
		key = self.lastKey[-1]
		for idx in range(1,len(arg)):
			self.visitStart(key)
			self.visitEnd(key)
			self.do("= ")
			self.visitStart(arg[idx]) 
			self.visitEnd(arg[idx])
			self.do("\n".ljust(self.depth + 1,"\t"))
	@visitEnd.register
	def _(self, arg :list):
		pass

class treeParser(object):
	"""Parsing a complex dict stucture 
	:param tree: The tree to parse ...
	:type tree : a dict wich can be walked
	:param filePath: The orginal file loction
	"""
	def __init__(self, filePath: Path, visitors : List[visitor] = [] ):
		self.filePath = filePath
		self.visitors = visitors

	def visit(self, treeNode):
		""" walk the tree with subscriders"""
		self.genericStart()
		for visitorObj in self.visitors:
			try:
				visitorObj.visitStart(treeNode)
				visitorObj.visitEnd(treeNode)
			except BaseException as error:
				print(f"error in object.visit on {sys._getframe().f_back.f_lineno} \n wit {error}")
				raise error


	def genericStart(self):
		print("genericStart called" )
		frame = Parser.db['Master']
		erro = True
		for idx , val in frame.iterrows():
			if val.Mode != "FileRegex":
				continue
			erro = False
			try:
				print("print( ",val.eval)
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



