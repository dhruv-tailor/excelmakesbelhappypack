import re, os
import Parser
import pathlib
import parradoxReader as PR
def test1():
	ModFolder = pathlib.PureWindowsPath(r"E:\Melle\Documents\Paradox Interactive\Europa Universalis IV\mod\GitBranch")
	files_ideas = [r"common\ideas\00_admin_ideas.txt" , r"common\ideas\00_dip_ideas.txt", r"common\ideas\00_mil_ideas.txt" ]
	files = [f for f in pathlib.Path(ModFolder /"common\\policies").iterdir() if pathlib.Path(f).suffix == ".txt"]

	out = []
	Parser.parser.main("")
	return
	path = pathlib.Path(ModFolder / files_ideas[0])
	if path.stat().st_size < 300:
		return #if the size is smaller than 300 bytes skip it
	data = PR.decode(path.as_posix(),False,False) 
	vissitor = Parser.dictVisitor()
	parser = Parser.treeParser(path,[vissitor])
	parser.visit(data)
	
if __name__ == "__main__":
	test1()

