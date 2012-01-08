#!/opt/local/bin/python

# import the Cheetah library
from Cheetah.Template import Template

# Satisfy the HTTP server's needs
print "Content-type: text/html\n"

# Instantiate a template file
t = Template(file="cheetahtest.tmpl")

# Print our template instance
print t

