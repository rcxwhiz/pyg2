import MessageHandler
import InputHandler
import FileSelectionHandler
import AssignmentHandler
import PathHandler
import os


def main() -> None:
	MessageHandler.printStartup()

	while True:
		print("\nMenu")
		print("-" * 25)
		print("Options:")
		print("[1] Grade/modify an existing assignment")
		print("[2] Create a directory for a new assignment")
		print("[0] Exit")

		choice = InputHandler.input_range(0, 2)

		if choice == 1:
			grade()
		if choice == 2:
			make_dir()
		if choice == 0:
			return None
		
		
def grade() -> None:
	print("Choose an assignment directory")
	assignmentDir = FileSelectionHandler.getDirectory(title="Open Assignment Directory")
	if assignmentDir == "":
		return None

	print("\nOptions:")
	print("[1] Generate key files")
	print("[2] Export key files")
	print("[3] Automatically grade student code")
	print("[4] Manually grade student code")
	print("[5] View a grading report")
	print("[0] Cancel\n")

	assignmentOption = InputHandler.input_range(0, 5)

	if assignmentOption == 1:
		PathHandler.createIfNot(PathHandler.join(assignmentDir, "key-source"))
		if len(os.listdir(PathHandler.join(assignmentDir, "key-source"))) == 1 and os.listdir(PathHandler.join(assignmentDir, "key-source"))[0].endswith(".py"):
			keyFile = os.listdir(PathHandler.join(assignmentDir, "key-source"))[0]
		else:
			print("Choose a key file")
			keyFile = FileSelectionHandler.getFile(title="Open Key File", filter_in="Python Files (*.py)", starting_dir=PathHandler.join(assignmentDir, 'key-source'))
			if keyFile == "":
				return None

		testsDir = PathHandler.join(assignmentDir, "test-cases")
		print(f"Using test cases from {testsDir}:")
		PathHandler.createIfNot(testsDir)

		if len(os.listdir(testsDir)) == 0:
			print("A default test case will be made")
			os.mkdir(testsDir)
		else:
			i = 1
			for testCase in os.listdir(testsDir):
				if os.path.isdir(testCase):
					print(f"{i}) {testCase}")
					i += 1
		AssignmentHandler.generateKeyFiles(keyFile, testsDir)

	if assignmentOption == 2:
		if not os.path.exists(PathHandler.join(assignmentDir, "test-cases")) or not os.path.exists(PathHandler.join(assignmentDir, "key-output")) or len(os.listdir(PathHandler.join(assignmentDir, "test-cases"))) == 0 or len(os.listdir(PathHandler.join(assignmentDir, "key-output"))) == 0:
			print("Cannot find test cases to export")
			print(f"{PathHandler.join(assignmentDir, 'test-cases')} or {PathHandler.join(assignmentDir, 'key-output')} are empty or missing")
			return None

		casesToExport = []
		for testCase in os.listdir(PathHandler.join(assignmentDir, "test-cases")):
			if testCase in os.listdir(PathHandler.join(assignmentDir, "key-output")):
				print(f"Include {testCase}?")
				print("[1] yes")
				print("[0] no")
				if InputHandler.input_range(0, 1) == 1:
					casesToExport.append(testCase)

		if len(casesToExport) > 0:
			AssignmentHandler.exportTestCases(assignmentDir, casesToExport)

	if assignmentOption == 3:
		for requiredFile in ["key-output", "test-cases", "ruberic.ini"]:
			if not os.path.exists(PathHandler.join(assignmentDir, requiredFile)):
				print(f"Could not find {PathHandler.join(assignmentDir, requiredFile)} which is requried")
				return None

	if assignmentOption == 4:
		print("help")

	if assignmentOption == 5:
		print("help")

	print("Returning to menu...")
		
		
if __name__ == "__main__":
	main()
