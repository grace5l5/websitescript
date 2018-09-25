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
	"filename": "content/blogs1.html",
	"output": "docs/blogs.html",
	"title": "My blogs",
	},
	{
	"filename": "content/contact.html",
	"output": "docs/contact.html",
	"title": "Contact me",
	},
]



blog_posts = [
	{
    "filename": "blog/1.html",
    "date": "September 3rd, 2018",
    "title": "My experience so far as a noob at Kickstart Coding",
	"output": "docs/blog1.html"
	},
	{
	"filename": "blog/2.html",
	"date": "September 10th, 2018",
	"title": "So far I really like Ubuntu Linux",
	"output": "docs/blog2.html"
	}, 
	{
	"filename": "blog/3.html",
	"date": "September 15th, 2018",
	"title": "My thoughts on Python so far",
	"output": "docs/blog3.html"
	}
]


def main():
# Iterate through the pages list and writes into the output file the title and the content
	blog_main()
	blog_pages()
	for page in pages:
		content = open(page['filename'])
		title = page['title']
		result_page = apply_title(title, content)
		open((page['output']),'w+').write(result_page)
		

def apply_title(title, content):
# Uses base.html as template to insert the title and content from the pages list
	base_page = open('base.html').read()
	index_content = content.read()
	incl_content_page = base_page.replace('{{content}}', index_content)
	finished_index_page= incl_content_page.replace('{{title}}', title)
	return finished_index_page


def blog_main():
# Replace the date of the blogs
	blog = open('content/blogs.html').read()
	date1 = blog.replace('{{date1}}', blog_posts[0]['date'])
	date2 = date1.replace('{{date2}}', blog_posts[1]['date'])
	date3 = date2.replace('{{date3}}', blog_posts[2]['date'])
	main_blog = date3.replace('{{date}}', blog_posts[len(blog_posts)-1]['title'])
	open('content/blogs1.html','w+').write(main_blog)


def blog_pages():
# Create blog page for each blog
	for blog in blog_posts:
		blog_template = open('blog/blog_template.html').read()
		blog_content = open(blog['filename']).read()
		blog_title = blog['title']
		published = blog['date']
		content_blog = blog_template.replace('{{content}}', blog_content)
		title_blog = content_blog.replace('{{title}}', blog_title)
		full_blog = title_blog.replace('{{date}}', published)
		open(blog['output'],'w+').write(full_blog)


if __name__ == "__main__":
    main()




