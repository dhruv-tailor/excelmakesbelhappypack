
import traceback , sys ,Parser , re, enum, math
from typing import List
from pathlib import Path
from Parser.IO import IO
from Parser.token import Token
from Parser.enums import *
import code


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
	errors = []

	@staticmethod
	def initialize( path : str,  game : str) :
		PL = ParserLocalisation
		loc = PL.localisation
		try:
			paths = [f for f in Path(f"Parser/statements/{game}/localisation").glob("*.yml")]
			for filePath in paths:
				if Path(filePath).is_file():
					try:
						IO.readLocalisation(filePath, ParserLocalisation.statements)
					except:
						traceback.print_exc()
			for key in PL.statements:
				if OPERATOR in PL.statements[key]:
					PL.operatorTypes.append(key);
			IO.readLookupRules("Parser/statements/{}/lookupRules.txt".format(game), ParserLocalisation.lookupRules);
			files = [f for f in Path(path + "/localisation").glob("*.yml")]
			for file in files:
				try:
					if "_l_english" in str(file):
						IO.readLocalisation(file, PL.localisation);
				except BaseException as error:
					traceback.print_exc()
			#code.interact(banner=None, readfunc=None, local=locals(), exitmsg=None)
			IO.readLocalisation("Parser/statements/operators.txt", PL.operators);
			IO.readExceptions("Parser/statements/{}/parentExceptions.txt".format( game), PL.parentExceptions)
			if (game == ("hoi4")):
				IO.readLocalisation("Parser/statements/hoi4/countries.txt", PL.localisation);

			variationFiles = {}
			IO.readLocalisation("Parser/statements/{}/variations.txt".format( game), variationFiles);
			for localisation, param in variationFiles.items():
				try :
					if (localisation[0] ==("#")):
						continue;
					params = param.split(", ");
					vars = []
					IO.readHeaders(path + params[0], vars, int(params[1]));
					for string in vars:
						ParserLocalisation.variations[string] = localisation
				except BaseException as error:
					raise Exception("Iligeall sate "+ error)
		except BaseException as error:
			traceback.print_exc()

	@staticmethod
	def localize(token :Token) :
		PL = ParserLocalisation
		localisation = None
		if token.type in PL.variations :
			return PL.formatString(PL.variations.get(token.type), token.operator, token.inverted,
					PL.findLocalisation(token.type), token.value);
		
		type = token.type;
		if (PL.getValueType(token) == ValueType.COUNTRY):
			type += "_country";
		if (PL.isParentException(token)):
			type = token.parent.type + "_" + type;
		if (PL.hasStatement(type)) :
			return PL.formatString(type, token.operator, token.inverted, localizeValue(token));
		else:
			if (localisation == None) :
				localisation = ParserLocalisation.getModifierLocalisation(type)
			if (localisation == None) :
				localisation = ParserLocalisation.getLocalisation(token.type);
			if (localisation == None) :
				PL.errors.append(token.type);
				#code.interact(banner=None, readfunc=None, local=locals(), exitmsg=None)
				return token.type + ": " + str(token.value);
			return localisation				

	@staticmethod
	def getModifierLocalisation(type : str) -> str:
		if type.lower() in ParserLocalisation.localisation:
			return ParserLocalisation.getLocalisation(type)
		type1 = type[:-9]
		types = [ type, type1, "modifier_" + type1 , "modifier_" + type,  type + "_MOD", "custom_idea_" + type ]
		for type2 in types:
			if type2.lower() in ParserLocalisation.localisation:
				return ParserLocalisation.getLocalisation(type2)

	@staticmethod
	def localizeValue(token : Token ) -> str : 
		type = ParserLocalisation.getValueType(token);
		if type == ValueType.PROVINCE:
			return getPrefixed("prov", token.value);
		elif type == ValueType.STATE:
			return getPrefixed("state", token.value);
		elif type == ValueType.DAYS or type == ValueType.MONTHS or type == ValueType.YEARS:
			val = int(token.value);
			if (val == -1):
				return "the rest of the campaign";
			elif (type == ValueType.DAYS) :
				if (val < 31):
					return str(val) + " days";
				elif (val < 365):
					return str(math.floor( val / 365 * 12)) + " months";
				else:
					return str(val / 365) + " years";
			else :
				return str(val) + " " + type.name.lower();
		elif type == ValueType.COUNTRY or type == ValueType.OTHER:
			if (ParserLocalisation.isCountry(token.value)) :
				return ParserLocalisation.getCountry(token.value);
			elif (ParserLocalisation.isLookup(token.value)):
				return ParserLocalisation.findLocalisation(token.value);
			elif (ParserLocalisation.isPercentage(token)):
				return ParserLocalisation.toPercentage(token.value);
			else:
				return token.value;
		else:
			raise Exception("Value type not found!");

	#/**
	# * Determines whether a given token value should be formatted as a percentage
	# * @param token The token
	# * @return Whether the token value should be formatted as a percentage
	# */
	@staticmethod
	def isPercentage( token : Token) -> bool :
		statement = ParserLocalisation.getStatement(token.type);
		if (statement == None) :
			return False;
		if re.fullmatch(number,token.value) is None:
			return False;
		return getStatement(token.type).contains("%%");
	
	#/**
	# * Turns a string into a percentage value
	# * @param value The value
	# * @return The value as a percentage
	# */
	@staticmethod
	def toPercentage( value : str) -> str :
		f = float(value);
		f *= 100;
		if (math.abs(f) >= 1):
			return "" + int(f);
		else:
			return "" + String.format(Locale.US, "%.1f", f);

	#/**
	# * Determines whether the parser should try to look up a given token value
	# * in the game localisation
	# * 
	# * @param value
	# *            The token's value
	# * @return Whether it should be looked up
	# */
	@staticmethod
	def isLookup( value : str) -> bool :
		if ((" ") in value):
			return False;
		try :
			float(value);
			return False;
		except ValueError as e:
			return True;

	#/**
	 #* Determines whether a given token value refers to a country
	 #* 
	 #* @param value
	 #*            The token's value
	 #* @return Whether it refers to a country
	 #*/
	@staticmethod
	def isCountry( value : str) -> bool :
		try :
			Scope.valueOf(value.toUpperCase());
			return true;
		except BaseException as e:
			return re.fullmatch(ParserLocalisation.country, (value)) != None and not value == ("yes");

	@staticmethod
	def getPrefixed(prefix : str, value : str) -> str :
		return ParserLocalisation.getLocalisation(prefix + value);

	#/**
	# * Attempts to find the game localisation for a given type or value
	# * 
	# * @param key
	# *            The type or value to be localised
	# * @return The localisation found. The key provided is returned if no
	# *         localisation is found
	# */
	@staticmethod
	def findLocalisation(key : str) -> str :
		key2 = key.replace("\"", "");
		loc = ParserLocalisation.getLocalisation(key2);
		if (loc != None) :
			return loc;
		loc = ParserLocalisation.getLocalisation("building_" + key2);
		if (loc != None) :
			return loc;
		loc = ParserLocalisation.getLocalisation(key2 + "_title");
		if (loc != None) :
			return loc;
		return key;
	#}
	
	#/**
	# * Looks up a string in the "localisation" map
	##* @param key The key to the string
	##* @return The string found. None if not found
	##*/
	@staticmethod
	def getLocalisation(key : str) -> str :
		try:
			return ParserLocalisation.localisation[key.lower()];
		except KeyError:
			return None
	#}
	
#**
#* Attempts to find the game localisation for a given scope
#* 
#* @param token
#*            The token to localise
#* @return The localisation found, plus formatting. None is
#*         returned if no localisation is found
#*/
	@staticmethod
	def getScopeLocalisation(token : Token) -> str :
		loc = None;
		while (True) :
			#if (regions.contains(token.type)) :
			#	loc = getLocalisation(token.type);
			if (loc != None) :
				break;
			loc = ParserLocalisation.getPrefixed("prov", token.type);
			if (loc != None) :
				break;
			loc = ParserLocalisation.getPrefixed("state_", token.type);
			if (loc != None) :
				break;
			if (ParserLocalisation.isCountry(token.type)) :
				loc = ParserLocalisation.getCountry(token.type);
				if (loc != None) :
					break;
			#}
			break;
		#}
		if (loc == None) :
			return None;
		#}
		if (token.inverted) :
			loc += " - none of the following";
		loc += ":";
		return loc;
	#}

	@staticmethod
	def getValueType(token : Token) -> ValueType :
		lookup = ParserLocalisation.lookupRules
		if token.type in lookup :
			type = ValueType[lookup[token.type].upper()];
			if type == ValueType.COUNTRY:
				if (not ParserLocalisation.isCountry(token.value)) :
					type = ValueType.OTHER;
			elif type == ValueType.PROVINCE or type == ValueType.STATE:
				if (ParserLocalisation.isCountry(token.value)) :
					type = ValueType.COUNTRY;
			else:
				pass;
			#}
			return type;
		#}
		else:
			return ValueType.OTHER;
	#}
	
#**
#* Gets a format string for a given token type
#* 
#* @param type
#*            The token type
#* @return The format string. None if not found
#*/
	@staticmethod
	def getStatement(key : str) -> str :
		try:
			return ParserLocalisation.statements[key.lower()];
		except KeyError:
			return None
	#}
	
#**
#* Determines whether localisation has been defined for a given token
#* @param token The token
#* @return Whether localisation is defined for it
#*/
	@staticmethod
	def hasStatement(key : str) -> bool :
		return key in ParserLocalisation.statements;
	#}
	@staticmethod
	def formatString(type : str, operator : Operator,inverted: bool,
			*values) -> str :
		if (inverted and not type in ParserLocalisation.operatorTypes) :
			type += "_false";
		statement = ParserLocalisation.getStatement(type);
		if (statement == None) :
			ParserLocalisation.errors.append(type);
			return statement;
		#}
		if ParserLocalisation.OPERATOR in statement :
			statement = insertOperator(statement, operator, inverted);
		return statement.format(values);
	#}

	@staticmethod
	def insertOperator(statement : str,  operator : Operator,inverted: bool) -> str :
		if (inverted) :# Opposite version is offset by one
			operator = Operator.values()[operator.ordinal() + 1];
		out = statement.replace(OPERATOR, operators.get(operator.toString().toLowerCase()));
		return out;
	#}
	
	@staticmethod
	def isParentException(token : Token) -> bool :
		vals = ParserLocalisation.parentExceptions.get(token.parent.type);
		return vals != None and (token.type) in vals;

		


	

		#/**
	 #* Looks up a country name
	 #* 
	 #* @param id
	 #*            The ID of the country
	 #* @return The country's name
	 #*/
	@staticmethod
	def getCountry(id :str) :
		if re.fullmatch(ParserLocalisation.country,id) is not None:
			return ParserLocalisation.getLocalisation(id);
		return str(Scope.valueOf(id.upper()))
