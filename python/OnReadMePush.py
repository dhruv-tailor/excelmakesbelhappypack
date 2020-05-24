
#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse , os, re, codecs
from itertools import islice
import subprocess

PARSER = argparse.ArgumentParser(description = """
On a push to this github it will read the reamde.MD and replace the loc file
Made by mellster""")
PARSER.add_argument("--output", metavar='Output Filename', default="../localisation/ML_ModPack_startup_l_english.yml", dest="output_filename", type=argparse.FileType('w'),
					help="The filename to use for the output file. Defaults to output-file.txt")
PARSER.add_argument("--input", metavar='input Filename', default="../README.md", dest="input_filename",  type=argparse.FileType('r'),
					help="The filename to use for the input file. Defaults to README.md")
PARSER.add_argument("--verionNumber", metavar='Verion number', default="v0.0.0", dest="version", help="the version number to use in out put")

ARGS = PARSER.parse_args()


template = """l_english:
 ###This file is made by {2} this file will be overwritten next time {3} is eddited
 ML_title_of_modpack.1:0 "{0}"
 ML_desc_of_modpack.1:0 "{1}"
""".format("{}","{}", os.path.basename(__file__), os.path.basename(ARGS.input_filename.name))
DefaultTitle = "Excelmakesbelhappypack {} Changelog ".format(ARGS.version) #"The excelmakesbelhappypack: {}".format(ARGS.version)
line_limit = 31

def escape(a_string):
	"""A custom function that escpaes qoutes and newlines in a string for use in l_english.yml files"""
	a_string = re.sub(r"#+([^\n\r]*)", "\u00A7G\\1\u00A7!" , a_string)
	trans = str.maketrans({"\\":  r"\\", #escape baklashes
										   "\n":  r"\n", # escape newlines and remvos coulurs
										   "#":  r"", 
										   "-":  r"\t", 
                                          "\"":  "\\\""}) #escape "
	return a_string.translate(trans)


def main():
	filename = ARGS.output_filename.name
	ARGS.output_filename.close()
	readme = ARGS.input_filename
	cmd = r"sed -n '/Changelog/,/endif/p' {} | sed -n '2,{}p'".format(readme.name, line_limit)
	#this command only runs on system with bash installed
	output = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	output = output.decode("latin-1")
	#print(output , error)
	print(escape(output))
	with codecs.open(filename, "w", "utf-8-sig") as outFile:
		title = escape(DefaultTitle)
		desc = escape(output)
		outFile.write(template.format(title, desc))
		
	with codecs.open(filename, "r", "utf-8-sig") as file:
		#print(file.read())
		pass
	print(filename)
if __name__ == "__main__":
	main()