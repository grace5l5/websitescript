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
	blog_page = blog_main()
	open('content/blogs1.html','w+').write(blog_page)
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
	main_blog1 = blog.replace('{{date1}}', blog_posts[0]['date'])
	main_blog2 = main_blog1.replace('{{date2}}', blog_posts[1]['date'])
	main_blog = main_blog2.replace('{{date3}}', blog_posts[2]['date'])
	return main_blog
'''

def blog_page():
	for count in range(len(blog_posts)):
		blog_template = open('blog_template.html').read()
		blog_content = open(blog_posts[count]['filename'])
		blog_title = blog_posts[count]['title']
		published = blog_posts[count]['date']
		content_blog = blog_template.replace('{{content}}', blog_content)
		title_blog = content_blog.replace('{{title}}', title)
		full_blog = title_blog.replace('{{date}}', date)
		return full_blog
'''

'''
bp_html = '<ol>'
for blog_post in blog_posts:
	bp_html = bp_html + '<li><a href="' + blog_post['title'] + '</a></li>'
bp_html

finished_index_page.replace('{{recent_blog_posts}}', bp_html)

'''

if __name__ == "__main__":
    main()




