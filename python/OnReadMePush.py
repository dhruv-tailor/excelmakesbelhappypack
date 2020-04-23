
import argparse , os, re, codecs
from itertools import islice

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
DefaultTitle = "The excelmakesbelhappypack: {}".format(ARGS.version)
a_string = "a test \" string \n"

def escape(a_string):
	"""A custom function that escpaes qoutes and newlines in a string for use in l_english.yml files"""
	a_string = re.sub("#+(.*)", r"§G\1§!" , a_string)
	return 	a_string.translate(str.maketrans({"\\":  r"\\", #escape baklashes
										   "\n":  r"\n", # escape newlines and remvos coulurs
										   "#":  r"", 
										   "-":  r"\t", 
                                          "\"":  "\\\""})) #escape "
	

def main():
	filename = ARGS.output_filename.name
	ARGS.output_filename.close()
	readme = ARGS.input_filename
	with codecs.open(filename, "w", "utf-8-sig") as outFile:
		title = escape(DefaultTitle)
		head = ''.join(list(islice(readme, 30)))
		desc = escape(head)
		outFile.write(template.format(title, desc))
		
		
	with codecs.open(filename, "r", "utf-8-sig") as file:
		print(file.read())

if __name__ == "__main__":
	main()