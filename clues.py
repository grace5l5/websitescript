
import glob 
import os

all_html_files = glob.glob("content/*.html")
#codes looked into the content folder and extract the file path all html files

pages = []

for content in all_html_files:
	file_path = content
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	#extracts the file name from the extension
	pages.append({
	"filename": file_name,
	"title": name_only,
	"output": "docs/" + file_name,
	})


for page in pages:
	print(page)





'''

#clue1

import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

output => ['content/blogs.html', 'content/blogs1.html', 'content/contact.html', 'content/index.html', 'content/projects.html']


#clue2
import os

file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)


output => 
blog.html
blog

#clue3

pages = []
pages.append({
	"filename": "content/index.html",
	"title": "Index",
	"output": "docs/index.html",
	})

print(pages)

output => [{'filename': 'content/index.html', 'title': 'Index', 'output': 'docs/index.html'}]

'''


