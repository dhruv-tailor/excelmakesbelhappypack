import re
import sys
import pathlib
from typing import List

class IO(object):
	"""description of class"""
	@staticmethod
	def getReader(fileName: str):
		print(fileName)
		if not pathlib.Path(fileName).exists():
			raise FileNotFoundError(fileName)
		return open(fileName, encoding="UTF8")
	@staticmethod
	def getANSIReader(fileName: str):
		print(fileName)
		if not pathlib.Path(fileName).exists():
			raise FileNotFoundError(fileName)
		return open(fileName, encoding= "Cp1252")

	##
	 # Reads a PDX-script file, reducing it to only the statements therein.
	 # Strips out comments, blank lines, and similar, and splits multiple
	 # statements on one line over multiple lines
	 #
	 # @param fileName
	 #            Name of the PDX-script file to be read.  Full file path or
	 #            relative path
	 # @return Linked list consisting of the processed output
	 # @throws IOException
	 #/
	@staticmethod
	def readFile(fileName:str) -> List[str]:
		lines = []
		with IO.getANSIReader(fileName) as In:
			for line in In:
				line = line.strip()
				# Get rid of comments
				commentIndex = line.find('#')
				if (commentIndex != -1):
					line = line[0:commentIndex]
				if line == "":
					continue
				# Handle brackets
				line = line.replace("{", "{\n", 1)
				line = line.replace("}", "\n}\n", 1)

				# Handle multiple actions in one line
				line = re.sub(r"([\\w.\"])\\s+(\\w+\\s#[=<>])", r"\1\n\2", line)

				start = 0
				end = line.find('\n')
				s = ""
				while True: # Substring and indexOf are used as it is faster than
						# StringTokenizer or split
					try:
						s = line[start: end ]
					except BaseException as error:
						s = line[start:] # Final part
					# Get rid of whitespace
					s = s.strip()
					if not (s == ""):
						lines.append(s)
					start = end + 1
					end = line.find('\n', start+1)
					if not (start != 0):
						break
				
		return lines


	
	##
	 # Reads a YAML localisation file.  Does not handle nesting
	 #
	 # @param fileName
	 #            Name of the localisation file to be read.  Full file path or
	 #            relative path
	 # @param map
	 #            Map to add the localisation to, rather than returning a map,
	 #            as one might often want to read several files into one map
	 # @param ignoreQuotes
	 #            If set to true, all quote-signs will be stripped out
	 # @throws IOException
	 #/
	@staticmethod
	def readLocalisation(fileName: str, Map:map) :
		with IO.getReader(fileName) as In:
			for line in In:
				# Remove all comments
				line = re.sub(r"#[^\"]*$", "",line)
			
				line = line.strip()
				# Remove localisation versioning  irrelevant to the parser
				line = re.sub(":\\d* ", ":",line)
				index = line.find(":")
				if (index == -1) :
					continue
				key = line[0: index].lower()
				# ":" used as delimiter, so index + 1
				value = line[index + 1:]
				value = re.sub(r"^\"(.*)\"$", r"\1", value)
				Map[key] = value

	##
	 # Reads a YAML-esque exceptions file.  Does not handle nesting
	 #
	 # @param fileName
	 #            Name of the file to be read.  Full file path or relative path
	 # @param map
	 #            Map to add the exceptions to
	 # @throws IOException
	 #/
	@staticmethod
	def readExceptions(fileName: str, Map: map) :
		with IO.getReader(fileName) as In:
			for line in In:
				line = line.strip()
				index = line.find(": ")
				if (index == -1) :
					continue
				key = line[0: index]
				# ": " used as delimiter, so index + 2
				values = line[index + 2:].split(", ")
				Map[key] = values

	##
	 # Reads a YAML-esque exceptions file.  Does not handle nesting
	 #
	 # @param fileName
	 #            Name of the file to be read.  Full file path or relative path
	 # @param map
	 #            Map to add the exceptions to
	 # @throws IOException
	 #/
	@staticmethod
	def readLookupRules(fileName: str, Map: map) :
		with IO.getReader(fileName) as In:
			for line in In:
				line = line.strip()
				index = line.find(": ")
				if (index == -1) :
					continue				
				value = line[0: index]
				# ": " used as delimiter, so index + 2
				keys = line[index + 2:].split(", ")
				for key in keys:
					Map[key] =  value

	##
	 # Writes a collection of strings to a file
	 #
	 # @param fileName
	 # @param contents
	 # @throws IOException
	 #/
	@staticmethod
	def writeFile(filename: str,  contents: List[str]) :
		out = open(fileName, "UTF8")
		for  string in contents:
			out.write(string + "\n")
		out.close()
	@staticmethod
	def readHeaders(fileName: str, headerList: List[str] , level: int):
		if not pathlib.Path(fileName).exists():
			raise Exception(f"file not exist: {filename}")
		if not pathlib.Path(fileName).is_dir():
			file = IO.readFile(fileName)
		else :
			paths = list(pathlib.Path(fileName).rglob('*.*'))
			file = []
			for path in paths:
				if not pathlib.Path(path).is_dir():
					file += IO.readFile(path)

		nesting = 0
		for line in file:
			line = line.strip().lower()
			if (line.endswith("{")) :
				if (nesting == level) :
					headerList.append(line.split("=")[0].strip().lower())
				nesting += 1
			elif (line == ("}")) :
				nesting -= 1
