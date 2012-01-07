#!/opt/local/bin/python

# import the Cheetah library
from Cheetah.Template import Template

# Satisfy the HTTP server's needs
print "Content-type: text/html\n"

# Instantiate a template file
t = Template(file="cheetahtest.tmpl")

# Variable 't', an instance of 
print t

