import MessageHandler
import InputHandler
import FileSelectionHandler
import AssignmentHandler


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
		AssignmentHandler.generateKeyFiles(assignmentDir)

	if assignmentOption == 2:
		AssignmentHandler.exportTestCases(assignmentDir)

	if assignmentOption == 3:
		AssignmentHandler.autoGrade(assignmentDir)

	if assignmentOption == 4:
		AssignmentHandler.manualGrade(assignmentDir)

	if assignmentOption == 5:
		AssignmentHandler.viewReport(assignmentDir)

	print("Returning to menu...")
		
		
if __name__ == "__main__":
	main()
