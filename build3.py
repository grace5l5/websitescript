pages = [
	{
	"filename": "content/index.html", 
	"output": "docs1/index.html",
	"title": "About me",
	},
	{
	"filename": "content/projects.html",
	"output": "docs1/projects.html",
	"title": "My Projects",
	},
	{
	"filename": "content/blogs.html",
	"output": "docs1/blogs.html",
	"title": "My blogs",
	},
	{
	"filename": "content/contact.html",
	"output": "docs1/contact.html",
	"title": "Contact me",
	},
]



def main():
	for count in range(len(pages)):
		content = open(pages[count]['filename'])
		resulting_html_for_index = apply_template(content)
		open((pages[count]['output']),'w+').write(resulting_html_for_index)


def apply_template(content):
# TODO: Read in template, do string replacing, and return result return results
	template = open('base.html').read()
	index_content = content.read()
	finished_index_page = template.replace('{{content}}', index_content)
	return finished_index_page



if __name__ == "__main__":
    main()

    