import ArgumentHandler
import PathHandler
import configparser
import shutil
import sys

reader = configparser.ConfigParser()


def resetConfig():
	print(f"Couldn't find {PathHandler.relJoin('config.ini')}")
	print('Creating default config file...')
	shutil.copyfile(PathHandler.relJoin('Config', 'default_config.ini'), PathHandler.relJoin('config.ini'))


if ArgumentHandler.resetConfig():
	resetConfig()

if ArgumentHandler.useDefaultOptions():
	try:
		reader.read(PathHandler.relJoin('ConfigHandler', 'default_config.ini'))
	except:
		print('Could not find a default config file. Exiting...')
		sys.exit()
else:
	try:
		reader.read(PathHandler.relJoin('config.ini'))
	except FileNotFoundError:
		resetConfig()
		reader.read(PathHandler.relJoin('config.ini'))

# General
showWarning = reader.getboolean('General', 'show_warning')
scoreDecimals = reader.getint('General', 'score_decimals')

# Runtime
maxThreads = reader.getint('Runtime', 'max_threads')
maxOutLines = reader.getint('Runtime', 'max_out_lines')
maxProgramTime = reader.getint('Runtime', 'max_program_time')

maxThreads = min(maxThreads, 500)
if maxThreads <= 0:
	maxThreads = 500

# Security/Restrictions
maxCodeLines = reader.getint('Security/Restrictions', 'max_code_lines')
phraseBlacklist = reader.get('Security/Restrictions', 'phrase_blacklist').split('\n')
phraseBlacklist[:] = [_ for _ in phraseBlacklist if _ != '']
packageWhitelist = reader.get('Security/Restrictions', 'package_whitelist').split('\n')
packageWhitelist[:] = [_ for _ in packageWhitelist if _ != '']
functionBlacklist = reader.get('Security/Restrictions', 'function_blacklist').split('\n')
functionBlacklist[:] = [_ for _ in functionBlacklist if _ != '']

if showWarning:
	original_file = open('config.ini', 'r', encoding='utf-8').read()
	open('config.ini', 'w', encoding='utf-8').write(
		original_file.replace('show_warning = true', 'show_warning = false'))
