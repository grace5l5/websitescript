
import utils
import sys

	""" Check for the number of arguments and if command is manage.py """
if len(sys.argv) > 1 and sys.argv[0] == 'manage.py':
	command = sys.argv[1]
	if command == "build":
		#runs the old commands
		utils.main()
		utils.content()
		print('Succesful ', command)
	elif command == "new":
		# create new page new_content_page.html
		utils.new()
		print('New content page created')
	else:
		print("Please specify ’build’ or ’new’")

	""" If User input has only one argument or argument is not equal to 'manage.py' """
else:
	print('''
	Usage:
	Rebuild site:		python manage.py build
	Create new page:	python manage.py new
		''')
