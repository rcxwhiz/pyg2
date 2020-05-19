import AssignmentHandler.FileVerification


def generateKeyFiles(assignmentDir: str) -> None:
	result = FileVerification.keyFiles(assignmentDir)
	if not result["success"]:
		print(result["errorMessage"])
		return None


def exportTestCases(assignmentDir: str) -> None:
	result = FileVerification.export(assignmentDir)
	if not result["success"]:
		print(result["errorMessage"])
		return None


def autoGrade(assignmentDir: str) -> None:
	print("help")


def manualGrade(assignmentDir: str) -> None:
	print("help")


def viewReport(assignmentDir: str) -> None:
	print("help")
