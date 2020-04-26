import pathlib
import parradoxReader as PR

class IdeaGroup:
	def __init__(self,name = "Empty idea/errpr" , type="", ideas=[], trigger="", Ideas = {}, json = {}):
		self.name = name
		self.typ = typ
		self.trigger = trigger
		self.ideas = ideas
		self.json = json
	def __repr__(self):
		ret = "IdeaGroup="+self.name + ": Type=" + self.type + " " + "Ideas:" + self.ideas.keys().__repr__()
		return ret



class IdeasGroupFactory:
	def ParseToJson(file):
		""" parse a file and output a list of ideas"""
		if not pathlib.Path(file).exists():
			 print('ERROR: Unable to find file: ' + str(file))
			 raise FileNotFoundError 
		if pathlib.Path(file).suffix != ".txt":
			print('ERROR: File not a .txt: ' + str(file))
		return PR.decode(pathlib.Path(file).as_posix(),False,True)
	def separateKeys(json, keys = ["category", "bonus" , "trigger", "ai_will_do", "important"]):
		""" Sperate the special keys"""
		keysDict = {}
		if type(keys) == str:
			if keys in json: del my_dict['key']
		if type(keys) == list:
			for ideaName in json:
				keysDict[ideaName] = {}
				for item in keys:
					if item in json[ideaName]: keysDict[ideaName][item] = json[ideaName].pop(item)
		return json , keysDict
	def makeIdeaGroup(json):
		ret = {}
		group, specKeys = IdeasGroupFactory.separateKeys(json)
		for name in group:
			try:
				trigger = specKeys[name].get('trigger', "")
				ret[name] = IdeaGroup(name, type=specKeys[name]["category"],
						 trigger=trigger,
						ideas= group[name],
						json=json[name] )
			except KeyError:
				raise KeyError
		return ret
	def ParseFromFile(file):
		out = IdeasGroupFactory.ParseToJson(file)
		return IdeasGroupFactory.makeIdeaGroup(out)