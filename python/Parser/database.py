import pandas as pd
from pathlib import Path
class database(object):
	"""object that holds data"""
	def __init__(self, path : Path = Path("Master.xlsx"),  *args, **kwargs):
		self.df = pd.read_excel(path.resolve(), header = 1, sheet_name = None)
		for sheet in self.df:
			print(self.df[sheet])
	
	def __getitem__(self, key):
		#print(self.df)
		return self.df[key]


