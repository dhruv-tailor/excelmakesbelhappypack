
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
		PL = ParserLocalisation
		try:
			paths = [f for f in Path(f"statements/{game}/localisation")]
			for filePath in paths:
				if Path(filePath).is_file():
					try:
						IO.readLocalisation(filePath, ParserLocalisation.statements)
					except:
						traceback.print_exc()
			for key in PL.statements:
				if PL.statements[key].contains(OPERATOR):
					operatorTypes.append(key);
			IO.readLookupRules("statements/{}/lookupRules.txt".format(game), lookupRules);
			files = [f for f in Path(path + "/localisation").glob("*.yml")]
			for file in files:
				try:
					if file.contains("_l_english"):
						IO.readLocalisation(file, localisation);
				except BaseException as error:
					traceback.print_exc()
			IO.readLocalisation("statements/operators.txt", operators);
			IO.readExceptions("statements/{}/parentExceptions.txt".format( game), parentExceptions)
			if (game.equals("hoi4")):
				IO.readLocalisation("statements/hoi4/countries.txt", localisation);

			variationFiles = {}
			IO.readLocalisation("statements/{}/variations.txt".format( game), variationFiles);
			for localisation, param in variationFiles.items():
				try :
					if (localisation.startsWith("#")):
						continue;
					params = param.split(", ");
					vars = {}
					IO.readHeaders(path + params[0], vars, int(params[1]));
					for string in vars:
						variations[string] = localisation
				except BaseException as error:
					raise Exception("Iligeall stae "+ error)
		except:
			traceback.print_exc()

	@staticmethod
	def localize(token :Token) :
		PL = ParserLocalisation
		if token.type in PL.variations :
			return PL.formatString(variations.get(token.type), token.operator, token.inverted,
					findLocalisation(token.type), token.value);
		
		type = token.type;
		if (PL.getValueType(token) == ValueType.COUNTRY):
			type += "_country";
		if (PL.isParentException(token)):
			type = token.parent.type + "_" + type;
		if (PL.hasStatement(type)) :
			return PL.formatString(type, token.operator, token.inverted, localizeValue(token));
		else:
			localisation = PL.getScopeLocalisation(token);
			if (localisation == None) :
				PL.errors.add(token.type);
				return token.type + ": " + token.value;
			return localisation				

		public static String localizeValue(Token token) {
		ValueType type = getValueType(token);
		switch (type) {
		case PROVINCE:
			return getPrefixed("prov", token.value);
		case STATE:
			return getPrefixed("state", token.value);
		case DAYS:
		case MONTHS:
		case YEARS:
			int val = Integer.parseInt(token.value);
			if (val == -1)
				return "the rest of the campaign";
			else if (type == ValueType.DAYS) {
				if (val < 31)
					return val + " days";
				else if (val < 365)
					return (int) ((float) val / 365 * 12) + " months";
				else
					return val / 365 + " years";
			} else 
				return val + " " + type.toString().toLowerCase();
		case COUNTRY:
		case OTHER:
			if (isCountry(token.value))
				return getCountry(token.value);
			else if (isLookup(token.value))
				return findLocalisation(token.value);
			else if (isPercentage(token))
				return toPercentage(token.value);
			else
				return token.value;
		default:
			throw new IllegalStateException("Value type not found!");
		}
	}