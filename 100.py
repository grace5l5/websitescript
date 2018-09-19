''' Advanced Challenge:
Experiment with the following code, and see if you can write code to
generate 100 pages, each that use the Bob Ross formatting, but just
display a single number in <h1></h1> tags.

for x in range(100):
    print(x)

Can you get them to each link to the next page, from page 1 to page 100?
'''

for x in range(100):
	title = x

	from string import Template

	top = open('templates/top.html').read()
	template = Template(top)
	bottom = open('templates/bottom.html').read()

	# Main landing page
	complete = template.safe_substitute(title='{}'.format(title))
	index = open('content/index.html').read() 
	total = complete + index + bottom 

	data = 'newdup/index' + str(x) + '.html'

	open(data, 'w+').write(total)

'''
title = 'title1'
complete = template.safe_substitute(title='{}'.format(title))
index = open('content/index.html').read() 
total = complete + index + bottom 
open('new/index.html', 'w+').write(total)

title = title2
'''
