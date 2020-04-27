import re, os
import Parser
import pathlib
import parradoxReader as PR
def test1():
	ModFolder = pathlib.PureWindowsPath(r"E:\Melle\Documents\Paradox Interactive\Europa Universalis IV\mod\GitBranch")
	files_ideas = [r"common\ideas\00_admin_ideas.txt" , r"common\ideas\00_dip_ideas.txt", r"common\ideas\00_mil_ideas.txt" ]
	files = [f for f in pathlib.Path(ModFolder /"common\\policies").iterdir() if pathlib.Path(f).suffix == ".txt"]
	out = []

	for f in files:
		data = PR.decode(pathlib.Path(f).as_posix(),False,False) 
		parser = Parser.treeParser(f, data)
		parser.walk()
		break

if __name__ == "__main__":
	test1()

