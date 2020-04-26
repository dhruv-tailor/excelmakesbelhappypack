import pandas as pd
from pathlib import Path
class database(object):
	"""object that holds data"""
	def __init__(self, path : Path = Path("Master.xlsx"),  *args, **kwargs):
		df = pd.read_excel(path.resolve(), header = 1, sheet_name = None)
		for sheet in df:
			print(df[sheet])
	


