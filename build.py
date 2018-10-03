import glob 
import os

all_html_files = glob.glob("content/*.html")
#codes looked into the content folder and extract the file path all html files

pages = []

for html_file in all_html_files:
	file_path = html_file
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	#extracts the file name from the extension
	pages.append({
	"filename": file_name,
	"title": name_only,
	"output": "docs/" + file_name,
	})

from jinja2 import Template

for page in pages:
	content = open('content/' + page['filename']).read()
	template_html = open("base.html").read()
	#using base.html as template
	template = Template(template_html)
	finish_page = template.render(
	title = page['title'],
	content = content,
	pages=pages,
	)
	open(page['output'], 'w+').write(finish_page)

