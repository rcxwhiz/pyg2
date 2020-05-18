import re
import ConfigHandler as cfg
import PathHandler

versionFinder = re.compile(r'[0-9]+\.[0-9]+[a-zA-Z]?')


def printStartup():
	print("PYthon Grader 2")
	try:
		print(f"Version - {re.search(versionFinder, open(PathHandler.relJoin('README.md'), 'r').read()).group()}")
	except:
		print("Couldn't find version in README.md")
	print("By Josh Bedwell")

	if cfg.showWarning():
		print("")
		print(open(PathHandler.relJoin('warning.txt')).read())
		print("")
