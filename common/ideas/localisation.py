#localisation\MEL_DevClick_l_english.yml
import re, sys

class localisation(dict):
    def __init__(self):
        self._mydict = {}
        setup(self)
    def __getitem__(self, key):
        #print(key)
        if hasattr(self,key):
            return getattr(self,key)
        print("Could not find {}".format(key))
        #find(key)
    def __setitem__(self, key, value):
        setattr(self, key, value)




def setup(self):
    files = [
        r"C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis IV\localisation\powers_and_ideas_l_english.yml",
        r"E:\Melle\Documents\Paradox Interactive\Europa Universalis IV\mod\GitBranch\localisation\Idea_Variation_ideas_l_english.yml",
        ]
    regex = r"\s?([\w\.]*?):.?\s\"(?:§\w\*+§\w)?([^\"§]+)"
    regex = re.compile(regex)
    for file in files:
        file = open(file, 'r', encoding="utf-8")
        for line in file:
            match = re.match(regex,line)
            if match is not None:
                self[match[1]]= match[2].strip()
        file.close()
        
    





if __name__ == "__main__":
	l = localisation()

    
    
