import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--default", action="store_true", help="Use default config values")
parser.add_argument("-r", "--reset", action="store_true", help="Reset config file")
args = parser.parse_args()


def getArgs() -> argparse.Namespace:
	return args


def useDefaultOptions() -> bool:
	return args.default


def resetConfig() -> bool:
	return args.reset
