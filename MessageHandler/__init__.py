import re
import ConfigHandler as cfg
import PathHandler

versionFinder = re.compile(r'\d+\.\d+[a-zA-Z]?')


def printStartup():
	print("PYthon Grader 2")
	try:
		print(f"Version - {re.match(versionFinder, open(PathHandler.relJoin('README.md'), 'r').read())}")
	except:
		print("Couldn't find README.md")
	print("By Josh Bedwell")

	if cfg.showWarning():
		print(open(PathHandler.relJoin('warning.txt')))
