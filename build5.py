from string import Template

pages = [
	{
	"filename": "content/index.html", 
	"output": "docs/index.html",
	"title": "About me",
	},
	{
	"filename": "content/projects.html",
	"output": "docs/projects.html",
	"title": "My Projects",
	},
	{
	"filename": "content/blogs.html",
	"output": "docs/blogs.html",
	"title": "My blogs",
	},
	{
	"filename": "content/contact.html",
	"output": "docs/contact.html",
	"title": "Contact me",
	},
]



def main():
# Iterate through the pages list and writes into the output file the title and the content
	for count in range(len(pages)):
		content = open(pages[count]['filename'])
		title = pages[count]['title']
		html_with_title = apply_title(title)
		resulting_html_for_index = apply_template(html_with_title, content)
		open((pages[count]['output']),'w+').write(resulting_html_for_index)


def apply_title(title):
# Uses base.html as template to insert the title from the pages list
	without_title = open('base.html').read()
	template = Template(without_title)
	with_title = template.safe_substitute(title= title)
	return with_title


def apply_template(html_with_title, content):
# Using the html from apply_title to insert content
	index_content = content.read()
	finished_index_page = html_with_title.replace('{{content}}', index_content)
	return finished_index_page


if __name__ == "__main__":
    main()

