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
		template = open('base.html').read()
		index_content = open(pages[count]['filename']).read()
		finished_index_page = template.replace('{{content}}', index_content)
		open((pages[count]['output']), 'w+').write(finished_index_page)


if __name__ == "__main__":
    main()

'''
template = open("base.html").read()
index_content = open("content/index.html").read()
finished_index_page = template.replace("{{content}}", index_content)
open("docs/index.html", "w+").write(finished_index_page)


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
	for count in range(len(pages)):
		top = open('templates/top.html').read()
		content = open(pages[count]['filename']).read()
		bottom = open('templates/bottom.html').read()
		final = top + content + bottom
		open((pages[count]['output']), 'w+').write(final)




if __name__ == "__main__":
    main()

'''