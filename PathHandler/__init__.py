import os
import sys


def mainScriptDir() -> str:
	return os.path.join(os.getcwd(), os.path.dirname(sys.argv[0]))


def relJoin(*args) -> str:
	result = mainScriptDir()
	for arg in args:
		result = os.path.join(result, arg)
	return result


def join(*args) -> str:
	result = ""
	for arg in args:
		result = os.path.join(result, arg)
	return result


def createIfNot(path: str) -> None:
	if not os.path.exists(path):
		os.makedirs(path)
