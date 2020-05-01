from Parser.token import Token
import traceback , sys, Parser, re
from typing import List
from pathlib import Path
from Parser.IO import Io
from Parser import Io


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