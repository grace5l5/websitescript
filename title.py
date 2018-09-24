from string import Template

top = open('templates/top.html').read()
template = Template(top)
bottom = open('templates/bottom.html').read()

# Main landing page
complete = template.safe_substitute(title='Grace Leung Shing')
index = open('content/index.html').read() 
total = complete + index + bottom 
open('docs/index.html', 'w+').write(total)

# contact
complete = template.safe_substitute(title='Contact Grace')
contact = open('content/contact.html').read() 
total = complete + contact + bottom 
open('docs/contact.html', 'w+').write(total)

# blogs
complete = template.safe_substitute(title='Blogs')
blogs = open('content/blogs.html').read() 
total = complete + blogs + bottom 
open('docs/blogs.html', 'w+').write(total)

# projects
complete = template.safe_substitute(title='Projects')
projects = open('content/projects.html').read() 
total = complete + projects + bottom 
open('docs/projects.html', 'w+').write(total)

