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

blog_posts = [
	{
    "filename": "blog/1.html",
    "date": "September 3rd, 2018",
    "title": "My experience so far as a noob at Kickstart Coding",
	},
	{
	"filename": "blog/2.html",
	"date": "September 10th, 2018",
	"title": "So far I really like Ubuntu Linux",
	}, 
	{
	"filename": "blog/3.html",
	"date": "September 15th, 2018",
	"title": "My thoughts on Python so far",
	}
]


def main():
# Iterate through the pages list and writes into the output file the title and the content
	for count in range(len(pages)):
		content = open(pages[count]['filename'])
		title = pages[count]['title']
		result_page = apply_title(title, content)
		open((pages[count]['output']),'w+').write(result_page)
	if blog_posts != []:
		blog_page()


def apply_title(title, content):
# Uses base.html as template to insert the title and content from the pages list
	base_page = open('base.html').read()
	index_content = content.read()
	finished_index_page = base_page.replace('{{title}}', title).replace('{{content}}', index_content)
	return finished_index_page

def blog_page():
	for count in range(len(blog_posts)):
		blog_template = open('blog_template.html').read()
		blog_content = open(blog_posts[count]['filename'])
		blog_title = blog_posts[count]['title']
		published = blog_posts[count]['date']
		full_blog = blog_template.replace('{{content}}', blog_content).replace('{{title}}', title).replace('{{date}}', date)
		return full_blog



if __name__ == "__main__":
    main()