
from Parser.token import Operator, Token
import traceback , sys, Parser
from typing import List
from pathlib import Path
from Parser.IO import IO
from Parser.ParserLocalisation import ParserLocalisation as Localisation


class parser(object):
	"""parser """
	namedBlocks = {}
	multiTokenExpressions = {}
	modifiers  = {}

	@staticmethod
	def parseTree(token : Token, output : List[str] ,  nesting : int, inverted : bool):
		out = ""
		toOutput = True

		if token.disabled:
			return

		if (parser.isInversion(token.type)):
			inverted = not inverted
			token.inverted = inverted
			nesting -= 1
			toOutput = False
		elif inverted :
			token.inverted = True 
			inverted = False  # Never persists past more than one level
		if 	(type(token.value) == str  and token.value.lower() == "no"):
				token.inverted = not token.inverted

		if (nesting == -1):
			out = "" 
		elif (nesting == 0):
			if (parser.isBlock(token)):
				out = parser.localize(parser.findName(token)) 
			else:
				out = "" 
		elif (nesting == 1 and not parser.isBlock(token)):
			out = "" 
		elif (parser.isMultiTokenExpression(token)) :
			parser.outputMultiLineCommand(token, output, nesting) 
			return  # Handles its own children
		elif (parser.isNamedBlock(token)):
			out = parser.localize( parser.findName(token)) 
		else:
			out = parser.localize(token) 
		if 'trigger' in str(out):
			pass
		if (toOutput):
			parser.output(out, output, nesting) 
		
		for child in token.children :
			parser.parseTree(child, output, nesting + 1, inverted) 

	@staticmethod
	def outputMultiLineCommand( token : Token,  output: List[str],  nesting : int) :
		associatedTypes =  parser.multiTokenExpressions.get(token.type, None) 
		length = len(associatedTypes) 
		values  = []
		modifierName = None 
		operator = token.operator 
		for i in range(0, length):
			found = False 
			target = associatedTypes[i] 
			for child in token.children:
				if (child.type == target) :
					values.append( parser.localizeValue(child)) 
					if (child.operator != Operator.EQUAL):
						operator = child.operator 
					if (parser.isModifier(child)):
						modifierName = child.value 
					found = True 
				elif child.type in (Localisation.variations) :
					variationName = Localisation.variations[child.type]
					if (variationName== (target)):
						values.append(Localisation.findLocalisation(child.type)) 
						values.append(localizeValue(child)) 
					found = True 
			if (not found and target == "duration"):
				values.append("the rest of the campaign")

		parser.output(Localisation.formatString(token.type, operator, token.inverted, values.copy()),
				output, nesting)
		if (modifierName != None) :
			effects = parser.modifiers.get(modifierName) 
			if (effects != None):
				for effect in effects:
					parser.output(effect, output, nesting + 1) 
		
	@staticmethod
	def isModifier( child: Token) -> bool:
		return child.type ==("name") 

	@staticmethod
	def localizeValue(token :Token) -> str:
		return Localisation.localizeValue(token) 

	@staticmethod
	def  localize(token :Token) -> str:
		return Localisation.localize(token) 

	@staticmethod
	def findName(token : Token)  -> Token :
		nameTokens = parser.namedBlocks.get(token.type)
		if type(nameTokens) == list:
			for string in nameTokens :
				for  child in token.children:
					if (string == (child.type)) :
						child.disabled = True 
						return child 
	
		print("No name found for " + str(token)) 
		return token 
		#throw new IllegalStateException("No name found!") 

	@staticmethod
	def   isBlock(token : Token) -> bool:
		return len(token.children) > 0 
	
	@staticmethod
	def   isNamedBlock(token : Token) -> bool:
		return parser.isBlock(token) and (token.type)  in parser.namedBlocks


	
	@staticmethod
	def  isMultiTokenExpression(token : Token) -> bool:
		return parser.isBlock(token) and (token.type)  in parser.multiTokenExpressions
	
	NEGATIONS = {"not", "nor" }

	##
	 # Determines whether a section inverts everything within it
	 # 
	 # @param type
	 #            The section name
	 # @return Whether it inverts everything within it
	 #/
	@staticmethod
	def isInversion(type : str) -> bool:
		return  type.lower() in parser.NEGATIONS  

	HEADER = "\n== {} ==" 
	BOLD = "\n'''{}'''\n" 
	
	##
	 # Formats a string based on how deeply nested it is, and adds it to the
	 # output collection
	 # 
	 # @param s
	 #            The string to be output
	 # @param output
	 #            The collection the formatted string is to be added to
	 # @param nesting
	 #            How deeply nested the string is
	 #/
	
	@staticmethod
	def  output(s : str,  output: List[str], nesting: str) :
		if (s == ("")):
			return  # Skip blank lines
		
		nesting -= 1 
		
		if (nesting <= -1) :
			output.append(parser.HEADER.format(str(s))) 
			return 
		elif (nesting == 0) :
			output.append(parser.BOLD.format(str(s))) 
			return 
		
		builder = "" 
		for i in range(0, nesting):
			builder += ('#') 
		builder +=(" ") 
		builder +=str(s) 
		output.append(builder) 
	
	##
	 # Reads all event modifiers and converts them to human-readable text, so
	 # that they can be displayed when a modifier is added
	 # 
	 # @param readFile
	 #            A formatted file containing modifiers
	 #/
	@staticmethod
	def  parseModifiers(root:Token) :
		PR = parser
		for child in root.children:
			effects = []
			name = child.type 
			for child2 in child.children:
				s = parser.localize(child2) 
				if s[0] >= '0' and s[0] <= '9':
					s = "+" + s 
				effects.append(s) 
			PR.modifiers[name] = effects


	@staticmethod
	def main(args : List[str]) :
		PR = parser
		settings = {}
		#print(Path('.').resolve())
		IO.readLocalisation("Parser/settings.txt", settings) 
		path = settings.get("path") 
		game = settings.get("game").lower() 
		
		Localisation.initialize(path, game) 
		
		IO.readExceptions("Parser/statements/{}/namedSections.txt".format( game), PR.namedBlocks) 
		IO.readExceptions("Parser/statements/{}/exceptions.txt".format( game), PR.multiTokenExpressions) 
		if (game == ("eu4")):
			PR.parseModifiers(Token.tokenizeFile(IO.readFile(path 
				+ "/common/event_modifiers/00_event_modifiers.txt"))) 
		

		def action (filePath) :
			if (Path(filePath).is_file()) :
				print("Parsing " + str(filePath)) 
				try :
					root = None
					with open(filePath, 'r',encoding='latin-1') as file:
						root = Token.tokenizeFile(file) 
					output = [] 
					parser.parseTree(root, output, -1, False) 
					Path("Parser/output").mkdir(parents=True, exist_ok=True)
					with open(Path("Parser/output") / filePath.name, 'w') as file:
						file.writelines(output)
				except BaseException as error:
					raise error
					traceback.print_exc()
		files= []
		for file in Path(Path(path)/ "events").glob("*.txt"):
			files.append(file)
			action(file)
		with open("Parser/output/errors.txt",'w') as file:
			for line in Localisation.errors:
				print(line, file=file)



