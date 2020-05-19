import sys
from typing import List

from PyQt5.QtWidgets import QApplication, QFileDialog

app = None
filterString = 'All Files (*);;Python Files (*.py);;Images (*.png *.jpg *.gif);;Text (*.txt);;CSV (*.csv)'
allFilesFilterString = 'All Files (*)'


def checkAppActive():
	global app
	if app is None:
		app = QApplication(sys.argv)


def getDirectory(title: str = 'Open folder', starting_dir: str = '') -> str:
	checkAppActive()
	to_return = QFileDialog.getExistingDirectory(None, title, starting_dir)
	return to_return


def getFile(title: str = 'Open file', filter_in: str = allFilesFilterString, starting_dir: str = '') -> str:
	checkAppActive()
	to_return, selected_filter = QFileDialog.getOpenFileName(None, title, starting_dir, filter_in)
	return to_return


def getFiles(title: str = 'Open files', filter_in: str = allFilesFilterString, starting_dir: str = '') -> List[str]:
	checkAppActive()
	to_return, selected_filter = QFileDialog.getOpenFileNames(None, title, starting_dir, filter_in)
	return to_return


def saveFile(title: str = 'Save file', filter_in: str = allFilesFilterString, starting_dir: str = '') -> str:
	checkAppActive()
	to_return, selected_filter = QFileDialog.getSaveFileName(None, title, starting_dir, filter_in)
	return to_return


if __name__ == '__main__':
	folder = getDirectory()
	choice = input()
	print('done')
