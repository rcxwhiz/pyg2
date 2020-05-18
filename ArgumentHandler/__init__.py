import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--default", action="store_true", help="Use default config values")
args = parser.parse_args()


def getArgs() -> argparse.Namespace:
	return args


def defaultArg() -> bool:
	return args.default
