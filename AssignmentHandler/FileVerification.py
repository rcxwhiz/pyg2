from typing import Dict
import PathHandler
import os
import FileSelectionHandler
import InputHandler


def keyFiles(assignmentDir: str) -> Dict:
	result = {}
	PathHandler.createIfNot(PathHandler.join(assignmentDir, "key-source"))
	if len(os.listdir(PathHandler.join(assignmentDir, "key-source"))) == 1 and os.listdir(PathHandler.join(assignmentDir, "key-source"))[0].endswith(".py"):
		result["keyFile"] = os.listdir(PathHandler.join(assignmentDir, "key-source"))[0]
	else:
		print("Choose a key file")
		result["keyFile"] = FileSelectionHandler.getFile(title="Open Key File", filter_in="Python Files (*.py)", starting_dir=PathHandler.join(assignmentDir, 'key-source'))
		if result["keyFile"] == "":
			result["success"] = False
			result["errorMessage"] = "Key file selection cancelled"
			return result

	result["testDir"] = PathHandler.join(assignmentDir, "test-cases")
	print(f"Using test cases from {result['testDir']}:")
	PathHandler.createIfNot(result["testDir"])

	result["tests"] = []
	if len(os.listdir(result["testDir"])) == 0:
		print("A default test case will be made")
		os.mkdir(PathHandler.join(result["testDir"], "default"))
		result["tests"].append(PathHandler.join(result["testDir"], "default"))
	else:
		i = 1
		for testCase in os.listdir(PathHandler.join(assignmentDir, result["testDir"])):
			if os.path.isdir(PathHandler.join(assignmentDir, result["testDir"], testCase)):
				result["tests"].append(PathHandler.join(assignmentDir, result["testDir"], testCase))
				print(f"{i}) {testCase}")
				i += 1

	result["success"] = True
	return result


def export(assignmentDir: str) -> Dict:
	result = {}
	if not os.path.exists(PathHandler.join(assignmentDir, "test-cases")) or not os.path.exists(
			PathHandler.join(assignmentDir, "key-output")) or len(
			os.listdir(PathHandler.join(assignmentDir, "test-cases"))) == 0 or len(
			os.listdir(PathHandler.join(assignmentDir, "key-output"))) == 0:
		result["success"] = False
		result["errorMessage"] = f"Cannot find test cases to export\n{PathHandler.join(assignmentDir, 'test-cases')} or {PathHandler.join(assignmentDir, 'key-output')} are empty or missing"
		return result

	result["cases"] = []
	for testCase in os.listdir(PathHandler.join(assignmentDir, "test-cases")):
		if testCase in os.listdir(PathHandler.join(assignmentDir, "key-output")):
			print(f"Include {testCase}?")
			print("[1] yes")
			print("[0] no")
			if InputHandler.input_range(0, 1) == 1:
				result["cases"].append(testCase)

	if len(result["cases"]) == 0:
		result["success"] = False
		result["errorMessage"] = "no test cases were found or selected"
	else:
		result["sucess"] = True
	return result


def autoGrade(assignmentDir: str) -> Dict:
	result = {}
	return result


def manualGrade(assignmentDir: str) -> Dict:
	result = {}
	return result


def viewReport(assignmentDir: str) -> Dict:
	result = {}
	return result
