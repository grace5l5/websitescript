
import utils
import sys

# Check for the number of arguments and if command is manage.py
if len(sys.argv) > 1 and sys.argv[0] == 'manage.py':
	command = sys.argv[1]
	print(command)
	if command == "build":
		utils.main()
		utils.content()
	elif command == "new":
		print("New page was specified")
	else:
		print("Please specify ’build’ or ’new’")

# User input is has only one argument or argument is not equal to 'manage.py'
else:
	print('''
	Usage:
	Rebuild site:		python manage.py build
	Create new page:	python manage.py new
		''')
