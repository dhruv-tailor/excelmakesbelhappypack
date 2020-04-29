
from Parser.token import Operator, Token 
import traceback , sys
from typing import List
from pathlib import Path

class parser(object):
	"""description of class"""
	namedBlocks = {}
	multiTokenExpressions = {}
	modifiers  = {}

	@staticmethod
	def parseTree(token : Token, output : List[str] ,  nesting : int, inverted : bool):
		out = ""
		toOutput = True

		if token.disabled:
			return

		if (isInversion(token.type)):
			inverted = not inverted
			token.inverted = inverted
			nesting -= 1
			toOutput = False
		elif inverted :
			token.inverted = True;
			inverted = False; # Never persists past more than one level
		if 	(type(token.value) == str  and token.value.lower() == "no"):
				token.inverted = not token.inverted

		if (nesting == -1):
			out = "";
		elif (nesting == 0):
			if (isBlock(token)):
				out = localize(findName(token));
			else:
				out = "";
		elif (nesting == 1 and not isBlock(token)):
			out = "";
		elif (isMultiTokenExpression(token)) :
			outputMultiLineCommand(token, output, nesting);
			return; # Handles its own children
		elif (isNamedBlock(token)):
			out = localize(findName(token));
		else:
			out = localize(token);
		
		if (toOutput):
			output(out, output, nesting);
		
		for child in token.children :
			parseTree(child, output, nesting + 1, inverted);

	@staticmethod
	def outputMultiLineCommand( token : Token,  output: List[str],  nesting : int) :
		associatedTypes = multiTokenExpressions.get(token.type, None);
		length = len(associatedTypes);
		values  = []
		modifierName = null;
		operator = token.operator;
		for i in range(0, length):
			found = False;
			target = associatedTypes[i];
			for child in token.children:
				if (child.type == target) :
					values.append(localizeValue(child));
					if (child.operator != Operator.EQUAL):
						operator = child.operator;
					if (isModifier(child)):
						modifierName = child.value;
					found = true;
				elif (Localisation.variations.containsKey(child.type)) :
					variationName = Localisation.variations.get(child.type);
					if (variationName.equals(target)):
						values.append(Localisation.findLocalisation(child.type));
						values.append(localizeValue(child));
					found = true;
			if (not found and target == "duration"):
				values.append("the rest of the campaign")

		output(Localisation.formatString(token.type, operator, token.inverted, values.copy()),
				output, nesting)
		if (modifierName != None) :
			effects = modifiers.get(modifierName);
			if (effects != None):
				for effect in effects:
					output(effect, output, nesting + 1);
		
		@staticmethod
		def isModifier( child: Token) -> bool:
		# TODO - Game-independent detection
			return child.type.equals("name");

	@staticmethod
	def localizeValue(token :Token) -> str:
		return Localisation.localizeValue(token);

	@staticmethod
	def  localize(token :Token) -> str:
		return Localisation.localize(token);

	@staticmethod
	def findName(token : Token)  -> Token :
		nameTokens = namedBlocks.get(token.type);
		for string in nameTokens :
			for  child in token.children:
				if (string.equals(child.type)) :
					child.disabled = true;
					return child;
	
		print("No name found for " + token);
		return token;
		#throw new IllegalStateException("No name found!");

	@staticmethod
	def   isBlock(token : Token) -> bool:
		return token.children.size() > 0;
	
	@staticmethod
	def   isNamedBlock(token : Token) -> bool:
		return isBlock(token) and namedBlocks.containsKey(token.type);

	
	@staticmethod
	def  isMultiTokenExpression(token : Token) -> bool:
		return isBlock(token) and multiTokenExpressions.containsKey(token.type);
	
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
		return NEGATIONS in (type.toLowerCase());

	HEADER = "\n== %s ==";
	BOLD = "\n'''%s'''\n";
	
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
		if (s.equals("")):
			return; # Skip blank lines
		
		nesting -= 1;
		
		if (nesting <= -1) :
			output.append(String.format(HEADER, s));
			return;
		elif (nesting == 0) :
			output.append(String.format(BOLD, s));
			return;
		
		builder = "";
		for i in range(0, nesting):
			builder += ('#');
		builder +=(" ");
		builder +=(s);
		output.append(builder.toString());
	
	##
	 # Reads all event modifiers and converts them to human-readable text, so
	 # that they can be displayed when a modifier is added
	 # 
	 # @param readFile
	 #            A formatted file containing modifiers
	 #/
	@staticmethod
	def  parseModifiers(root:Token) :
		for child in root.children:
			effects = []
			name = child.type;
			for child2 in child.children:
				s = localize(child2);
				if s[0] >= '0' and s[0] <= '9':
					s = "+" + s;
				effects.append(s);
			modifiers.put(name, effects);


	@staticmethod
	def main(args : List[str]) :
		settings = {}
		IO.readLocalisation("settings.txt", settings);
		path = settings.get("path");
		game = settings.get("game").toLowerCase();
		
		Localisation.initialize(path, game);
		
		IO.readExceptions(String.format("statements/%s/namedSections.txt", game), namedBlocks);
		IO.readExceptions(String.format("statements/%s/exceptions.txt", game), multiTokenExpressions);
		if (game.equals("eu4")):
			parseModifiers(Token.tokenize(IO.readFile(path 
				+ "/common/event_modifiers/00_event_modifiers.txt")));
		

		def action (filePath) :
			if (Files.isRegularFile(filePath)) :
				print("Parsing " + filePath.getFileName());
				try :
					root = None
					with open(filePath.toString(), 'r') as file:
						root = Token.tokenize(file);
					output = [];
					parseTree(root, output, -1, false);
					# TODO - Ensure output folder exists
					Path("output").mkdir(parents=True, exist_ok=True)
					with open("output/" + filePath.getFileName(), 'w') as file:
						file.writelines(output)
				except BaseException as error:
					traceback.print_exc()
		files = sorted(Path(path/ "events").glob("*.txt"))
		map(action, files)
		Files.walk(Paths.get(path + "/events"));
		with open("output/errors.txt",'w') as file:
			file.writeLines(Localisation.errors)

	# TODO - Properly handle calling other events
	# TODO - Handle event headers (E.G., is_mtth_scaled_to_size)
