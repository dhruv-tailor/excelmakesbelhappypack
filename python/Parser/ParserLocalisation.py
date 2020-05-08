
import traceback , sys ,Parser , re, enum
from typing import List
from pathlib import Path
from Parser.IO import IO

class Operator(enum.Enum):
	LESS = 0 
	NOTLESS = 1 
	MORE = 2
	NOTMORE = 3
	EQUAL = 4 
	NOTEQUAL = 5

class ValueType(enum.Enum):
	COUNTRY = 0
	PROVINCE = 1
	STATE = 2
	DAYS =3
	MONTHS =4
	YEARS = 5
	OTHER = 6
class Scope(enum.Enum):
	ROOT= 0 
	THIS= 1
	FROM= 2 
	CONTROLLER= 3
	OWNER= 4
	PREV = 5
	def __str__(self):
		if self == Scope.ROOT:
			return "our country";
		elif self == Scope.THIS:
			return "this country";
		elif self == Scope.FROM:
			return "from"
		elif self == Scope.CONTROLLER:
			return "the province's controller";
		elif self == Scope.OWNER:
			return "the province's owner";
		elif self == Scope.PREV:
			return "the previous scope";
		else:
			raise Exception(str(self) + " is an unlocalized enum.");

class ParserLocalisation(object):
	"""description of class"""
	lookupRules = {}
	localisation = {}
	statements = {}
	operators = {}
	variations = {}
	operatorTypes = {}
	parentExceptions = {}
	country = re.compile("[a-zA-Z]{3}")
	number = re.compile("-?\\d+\\.?\\d*");
	OPERATOR = "[OPERATOR]";

	@staticmethod
	def initialize( path : str,  game : str) :
		try:
			paths = [f for f in Path(f"statements/{game}/localisation")]
			for filePath in paths:
				if Path(filePath).is_file():
					try:
						IO.readLocalisation(filePath, ParserLocalisation.statements)
					except:
						traceback.print_exc()
		except:
			pass
						