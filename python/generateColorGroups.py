#pip install colormath

import os
import re

import argparse

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

#Script Args
PARSER = argparse.ArgumentParser(description = "Process EU4 country files to define similar color groups. \n\nThis script will scan all country tags, attempt to load their country file, use CIE2000 to parse the color of the country, and group them together in order. \n\n Countries earlier in the country tags lists will have preference, and become the basis for the groups. \n\n Outputs a list of CB definitions.")
PARSER.add_argument("--variance", metavar='Color Variance', type=int, default=10, dest="variance", help="The maximum distance two colors can be before splitting into a new group. This is a measurement of Delta E from CIE2000 Defaults to 10.")
PARSER.add_argument("--output", metavar='Output Filename', default="output-file.txt", dest="output_filename", help="The filename to use for the output file. Defaults to output-file.txt")
PARSER.add_argument("--outputencoding", metavar="Output File Encoding", default="ANSI", dest="output_encoding", help="The file encoding to use when writing the output file. Defaults to ANSI.")
PARSER.add_argument("--inputencoding", metavar="Input File Encoding", default="ANSI", dest="input_encoding", help="The file encoding to use when reading tag and country files. Defaults to ANSI.")
PARSER.add_argument("--input", metavar="Common folder", default=["common"], nargs="*", dest="commons", help="A list of 'common' folders to process. Will only generate one output file, regardless of number of folders.")

ARGS = PARSER.parse_args()

#Regex patterns for parsing files.
COLOR_PATTERN = re.compile(r"^color\s=\s{\s(\d+)\s*(\d+)\s*(\d+)\s*}", re.MULTILINE)
TAG_PATTERN = re.compile(r"^(\w{3})\s*=\s*\"(.*)\"", re.MULTILINE)

TAGS = dict()
GROUPS = dict()
NAMES = dict()

#templates for building the CBs

#main CB block
cb_block = """
cb_color_{0} = {{
    valid_for_subject = no
    prerequisites = {{
        NOT = {{
            truce_with = FROM 
        }}
        ai = no
        OR = {{
{1}
        }}
        OR = {{
{2}
        }}
    }}
    
    war_goal = take_border
}}
"""
#Template for is neighbor of a tag
neighbor_template = "            is_neighbor_of={0}"

#template to check if the player is one of the tags
tag_template = "            tag={0}"


def parse_tags_file(filename, common):
    country_tags = open(filename, 'r', encoding=ARGS.input_encoding)
    for line in country_tags:
        result = TAG_PATTERN.match(line)
        if result:
            tag = result.group(1)
            country_file = result.group(2)
            
            TAGS[tag] = os.path.join(common, country_file)
            NAMES[tag] = os.path.basename(country_file)[:-4]

    country_tags.close()

def process_country(tag, filename):
    textfile = open(filename, 'r', encoding=ARGS.input_encoding)
    for line in textfile:
        result = COLOR_PATTERN.match(line)
        if result:
            colorparts = [int(_)/255 for _ in result.group(1, 2, 3)]

            rgb = sRGBColor(colorparts[0], colorparts[1], colorparts[2])
            lab = convert_color(rgb, LabColor)

            #Test all groups for similarity
            for key in list(GROUPS):
                delta_e = delta_e_cie2000(lab, key)
                if delta_e <= ARGS.variance:
                    GROUPS[key][1].append(tag)
                    return

            #No group matches, 
            GROUPS[lab] = (tag, list()) #GROUPS[key][0] contains the originator tag for the color.
            GROUPS[lab][1].append(tag)
            break
    textfile.close()


for common in ARGS.commons:
    common = os.path.join(".", common)

    country_tags = os.path.join(common, "country_tags")
    print("Processing Country Tags: {0}".format(country_tags))
    for filename in os.listdir(country_tags):
        # Load all the tags from the country tags files.
        # If a tag already existed, we're going to clear it's group.
        parse_tags_file(os.path.join(country_tags, filename), common)
    
        
print("Processing {0} Tags".format(len(TAGS)))
for tag in list(TAGS):
    # Process the country file for each tag
    process_country(tag, TAGS[tag])
    print('.', end='', flush=True)


print("\nIdentified {0} unique colors".format(len(list(GROUPS))))

# Generate output.

output = open(ARGS.output_filename, "w", encoding=ARGS.output_encoding)
output.write("# This file was genrated by {0}".format(os.path.basename(__file__)))
for i, v in enumerate(list(GROUPS)):
    if len(GROUPS[v][1]) <= 1:
        continue
    tags = ""
    neighbors = ""

    for tag in GROUPS[v][1]:
        tags += tag_template.format(tag).ljust(30)
        tags += "#" + NAMES[tag] + '\n'
        neighbors += neighbor_template.format(tag).ljust(35)
        neighbors += "#" + NAMES[tag] + '\n'

    output.write(cb_block.format(i, neighbors, tags))
    output.write("\n\n")
for itter in range(1,len(list(GROUPS))):
    output.write(""" cb_color_{0}_desc:0 "People have been complaining about Unresolved Margins, Color disputes, Precarious Perimeters and a Chroninc Chromatic Conflict between out nations. It needs to be resolved on the battlefield."
 cb_color_{0}:0 "Misplaced Border\n""".format(itter))
output.close()
