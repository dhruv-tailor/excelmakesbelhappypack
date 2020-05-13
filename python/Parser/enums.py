import enum
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