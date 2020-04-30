import re, enum
from typing import List
from pathlib import Path
from codecs import StreamReader
from Parser.ParserLocalisation import Operator


class Token(object):
	"""description of class"""

	inverted = False
	disabled = False
	def __init__(self, Type : str, value: str, operator : object, parent ):
		super().__init__()
		self.type = Type.lower()
		if value is not None:
			self.value = None
		else:
			self.value = repr.sub("^\"(.*)\"$", "\1", value);
		self.operator = operator
		self.parent = parent
		if parent is not None:
			parent.add(self)
		self.children = []
		@clsmethod
		def tokenize(cls, s :str,  parent: Token) -> cls:
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
				return cls(s[:index].strip(), s[index:].strip(), operator, parent)

		@classmethod
		def tokenizeFile(cls, fileStream : StreamReader ) -> Token:
			root = cls("file", None, None,None)
			block = root
			lines = files.readlines()
			for string in lines:
				if string == "}":
					block = block.parent
				elif string.find('{') != -1:
					block = tokenize(string , block)
				else:
					tokenize(string , block)
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



