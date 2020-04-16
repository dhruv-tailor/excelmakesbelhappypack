import parradoxReader as PR
import pathlib 
import os
import json
import random

class Ideas:
	def __init__(self,name, typ, listgroups, trigger):
		self.name = name
		self.typ = typ
		self.listgroups = listgroups
		self.trigger = trigger

def test1():
	ModFolder = pathlib.PureWindowsPath("../..")
	files = ["00_basic_ideas.txt" , "00_flogi_ideas.txt" ]
	#files = [f for f in os.listdir('.') if os.path.isfile(f)]
	out = []
	print (pathlib.Path('.'))
	for f in files:
		f = ModFolder / "common" /  "ideas" / f 
		if pathlib.Path(f).suffix == ".txt":
			data = PR.decode(pathlib.Path(f).as_posix(),False,False)
			out.append(data)
	list = []
	data = out[0]
	for f in out[1:]:
		data.update(f)
	for name in data:
		item =  data[name]
		if type(item)  == type(list):
			item1 = item[1]
			item = item[0]
		listgroups = []
		effects = []
		typ = item["category"]
		if "trigger" in item:
			trigger = item["trigger"]
		else:
			trigger = "always = yes"
		#print(typ)
		for key in item:
			if key in ["category", "bonus" , "trigger", "ai_will_do"]:
				continue
			listgroups.append(key)
		list.append(Ideas(name, typ, listgroups.copy(), trigger))
		listgroups.clear()
		effects.clear()
	count = 0
	outfile = open("pythonout.txt.tmp","w")
	for name in data:
		count = count + 1
		if (count % 10 == 1):
			outfile.write("""	GetIdeas = {
		variable_name = numOfFreeIdeas \n""")
		outfile.write("\t\tid" + str(count% 10)+"=" + name + '\n')
		if (count % 10 == 0):
			outfile.write("}\n")
	outfile.write("}")
	outfile.close()
	template = """Add{0} = {{
	if = {{ limit = {{ check_variable = {{ which = numOfFreeIdeas value = 1	}} }}
	if = {{ limit = {{  {1}	  }}
	add_idea_group = {0}	}}"""
	template1 = """	if = {{ limit = {{ check_variable = {{ which = numOfFreeIdeas value = 1	}} }} add_idea = {0}
		if = {{ limit = {{ has_idea = {0} }} subtract_variable = {{ which = numOfFreeIdeas value = 1 }}	}} }}"""
	outfile = open("ML_AddIdeas.txt.tmp","w")
	for ideaG in list:
		outfile.write(template.format(ideaG.name, PR.encode(ideaG.trigger)) + '\n')
		for idea in ideaG.listgroups:
			outfile.write(template1.format(idea) + '\n')
		outfile.write("}\t }\n")
	for ideaG in list:
		outfile.write("#Add{0}\n".format(ideaG.name))
	outfile.close()
	
	for itter in range(1,6):
		random.shuffle(list)
		outfile = open("ML_ideaordereffect{0}.txt.tmp".format(itter),"w")
		outfile.write("ideaorder{0} = {{\n".format(itter))
		for ideaG in list:			
			outfile.write("\tAdd{0} = yes\n".format(ideaG.name))
		outfile.write("}\n")
		outfile.close()
if __name__ == "__main__":
	test1()
