import re, enum
from typing import List
from pathlib import Path
from codecs import StreamReader
from Parser.enums import Operator


class Token(object):
	"""description of class"""

	inverted = False
	disabled = False
	def __init__(self, Type : str, value: str, operator : object, parent ):
		super().__init__()
		self.type = Type.lower()
		if value == '{ # favour local nobles':
			pass
		if value is None:
			self.value = None
		else:
			self.value = re.sub(r"^\"(.*)\"$", r"\1", value);
		self.operator = operator
		self.parent = parent
		if parent is not None:
			parent.children.append(self)
		self.children = []
	@classmethod
	def tokenize(cls, s :str,  parent : object) -> object:
		"""	/**
			* Creates a token from a given string and its parent token
			* @param s The string to turn into a token
			* @param parent The block it is contained within
			* @return The created token
			*/"""
		operator = None
		index = -1
		if s.find('=') != -1:
			operator = Operator.EQUAL
			index = s.find('=')

		if index == -1:
			return cls(s, None,None,parent)
		else:
			return cls(s[:index].strip(), s[index+1:].strip(), operator, parent)

	@classmethod
	def tokenizeFile(cls, lines ) -> object:
		if type(lines) != list :
			root = cls("file", lines.name, None,None)
		else:
			root = cls("file", None, None,None)
		block = root
	
		for i, string in enumerate(lines):
			if string == "}":
				block = block.parent
			elif string.find('{') != -1:
				block = Token.tokenize(string , block)
			else:
				Token.tokenize(string , block)
		return root
	def __str__(self) -> str:
		if self.value is None:
			return self.type
		else:
			op = ""
			if self.operator == Operator.LESS:
				op = '<'
			elif self.operator == Operator.EQUAL:
				op = "="
			else:
				raise Exception("Invalid operator!")
			return "{} {} {}".format(self.type, op , self.value)



