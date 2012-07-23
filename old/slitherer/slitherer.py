###############################################
# slitherer.py
#
# This is PyBros' data 'slitherer', cause we
#  don't crawl, we slither.
#  
# 2012-07-19
# Trevor Pottinger
###############################################

from aquire import url_feeder, url_grabber
from prune import data_extractor, data_cleanser
from eat import database_feeder

class slitherer(object):
	def __init__(self):
		self.feeder = url_feeder('sp500.csv')
		self.grabber = url_grabber()
		self.extractor = data_extractor(self.feeder)
		self.cleaner = data_cleanser()
		self.eater = database_feeder('root', 'pybros', 'rev3')

	def slither(self):
		i = 0
		for (url,appetizer) in self.feeder:
			i += 1
			print i
			html = self.grabber.retrieve(url)
			if html == '':
				continue # maybe something else?
			datalist = self.extractor.extract(html)
			dinner = self.cleaner.cook(datalist)
			self.eater.eat(dinner, appetizer)

def main():
	pybros = slitherer()
	pybros.slither()

if __name__ == '__main__':
	main()
