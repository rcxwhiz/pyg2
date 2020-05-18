import ConfigHandler.ConfigGetter
from typing import List


def showWarning() -> bool:
	return ConfigGetter.showWarning


def scoreDecimals() -> bool:
	return ConfigGetter.scoreDecimals


def maxThreads() -> int:
	return ConfigGetter.maxThreads


def maxOutLines() -> int:
	return ConfigGetter.maxOutLines


def maxProgramTime() -> float:
	return ConfigGetter.maxProgramTime


def maxCodeLines() -> int:
	return ConfigGetter.maxCodeLines


def phraseBlacklist() -> List[str]:
	return ConfigGetter.phraseBlacklist


def packageWhitelist() -> List[str]:
	return ConfigGetter.packageWhitelist


def functionBlacklist() -> List[str]:
	return ConfigGetter.functionBlacklist
