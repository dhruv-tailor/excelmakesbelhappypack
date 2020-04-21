import parradoxReader as PR
import pathlib 
import os, json, random
import localisation

class Ideas:
	def __init__(self,name, typ, listgroups, trigger):
		self.name = name
		self.typ = typ
		self.listgroups = listgroups
		self.trigger = trigger

def test1():
	ModFolder = pathlib.PureWindowsPath(r"E:\Melle\Documents\Paradox Interactive\Europa Universalis IV\mod\GitBranch")
	files = [r"common\ideas\00_admin_ideas.txt" , r"common\ideas\00_dip_ideas.txt", r"common\ideas\00_mil_ideas.txt" ]
	#files = [f for f in os.listdir('.') if os.path.isfile(f)]
	loc = localisation.localisation()
	out = []
	print (pathlib.Path('.'))
	for f in files:
		f = ModFolder / pathlib.Path(f)
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
	introText = "#This file was genrated by {0}\n".format(os.path.basename(__file__))
	template = """Add{0} = {{
	if = {{ limit = {{ check_variable = {{ which = numOfFreeIdeas value = 1	}} }}\n	if = {{ limit = {{  {1}	  }}
	add_idea_group = {0}	}}"""
	template1 = """	if = {{ limit = {{ check_variable = {{ which = numOfFreeIdeas value = 1	}} }} add_idea = {0}
		if = {{ limit = {{ has_idea = {0} }} subtract_variable = {{ which = numOfFreeIdeas value = 1 }}	}} }}"""
	outfile = open("ML_AddIdeas.txt.tmp","w")
	outfile.write(introText)
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
		outfile.write(introText)
		outfile.write("ideaorder{0} = {{\n".format(itter))
		for ideaG in list:			
			outfile.write("\tAdd{0} = yes\n".format(ideaG.name))
		outfile.write("}\n")
		outfile.close()

	template2 = """ideaorderSmart{0} = {{\n """
	template3a = "\t if = {{ limit = {{ has_idea_group = {0} }} "
	template3b = "Add{0} = yes }}"
	template3c = "#{0}\n "
	for itter in range(1,2):
		random.shuffle(list)
		outfile = open("ML_ideaordereffectSmart{0}.txt.tmp".format(itter),"w")
		outfile.write(introText)
		outfile.write(template2.format(itter))
		for ideaG in list:			
			outfile.write(template3a.format(ideaG.name).ljust(60," "))
			outfile.write(template3b.format(ideaG.name).ljust(45," "))
			outfile.write(template3c.format(loc[ideaG.name]))
		outfile.write("}\n")
		outfile.close()
	with open("ML_ideaordereffectSmart1.txt.tmp","r") as file:
		return(file.read())
	
if __name__ == "__main__":
	test1()
