from string import Template

pages = [
	{
	"filename": "content/index.html", 
	"output": "docs2/index.html",
	"title": "About me",
	},
	{
	"filename": "content/projects.html",
	"output": "docs2/projects.html",
	"title": "My Projects",
	},
	{
	"filename": "content/blogs.html",
	"output": "docs2/blogs.html",
	"title": "My blogs",
	},
	{
	"filename": "content/contact.html",
	"output": "docs2/contact.html",
	"title": "Contact me",
	},
]


def main():
# Iterate through the pages list and writes into the output file the title and the content
	for count in range(len(pages)):
		content = open(pages[count]['filename'])
		title = pages[count]['title']
		result_page = apply_title(title, content)
		open((pages[count]['output']),'w+').write(result_page)


def apply_title(title, content):
# Uses base.html as template to insert the title and content from the pages list
	base_page = open('base.html').read()
	index_content = content.read()
	finished_index_page = base_page.replace('{{title}}', title).replace('{{content}}', index_content)
	return finished_index_page


if __name__ == "__main__":
    main()
