filenames = ['templates/top.html', 'content/index.html', 'templates/bottom.html']
with open('docs/index.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['templates/top.html', 'content/contact.html', 'templates/bottom.html']
with open('docs/contact.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['templates/top.html', 'content/blogs.html', 'templates/bottom.html']
with open('docs/blogs.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['templates/top.html', 'content/projects.html', 'templates/bottom.html']
with open('docs/projects.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())