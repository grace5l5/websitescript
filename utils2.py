import glob 
import os
from jinja2 import Template

pages = []

blogs = []

def main():
	all_html_files = glob.glob("content/*.html")
	# codes looked into the content folder and extract the file path all html files

	for html_file in all_html_files:
		file_path = html_file
		file_name = os.path.basename(file_path)
		name_only, extension = os.path.splitext(file_name)
		# extracts the file name from the extension
		global pages
		# Will fix it so that it is a return 
		pages.append({
		"filename": file_name,
		"title": name_only,
		"output": "docs/" + file_name,
		})

def nav_bar():
	for page in pages:
		template_html = open("base.html").read()
		template = Template(template_html)
		with_nav = template.render(
			pages=pages,
			)
	print(with_nav)

'''
def content():
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


def new():
	template = '''
#	<h1> New Content! </h1>

#	<p> New content... </p>
	'''
	open('content/new_content_page.html', 'w+').write(template)


def blog():
	all_blog_files = glob.glob("blog/*.html")
	# codes looked into the content folder and extract the file path all html files 

	for blog_file in all_blog_files:
		blog_path = blog_file
		blog_name = os.path.basename(blog_path)
		blog_name_only, extension = os.path.splitext(blog_name)
		#extracts the file name from the extension
		global blogs
		blogs.append({
		"blogname": blog_name,
		"title": blog_name_only,
		"output": "docs/" + blog_name,
		})


def blog_content():
	for blog in blogs:
		content = open('blog/' + blog['blogname']).read()
		template_html = open("base.html").read()
	#using base.html as template
		template = Template(template_html)
		finish_blog = template.render(
		title = blog['title'],
		content = content,
		blogs=blogs,
		)
		open(blog['output'], 'w+').write(finish_blog)

