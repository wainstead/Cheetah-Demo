#!/opt/local/bin/python

from datetime import datetime

# import the Cheetah library
from Cheetah.Template import Template

# Satisfy the HTTP server's needs
print "Content-type: text/html\n"

# Instantiate a template file
t = Template(file="cheetahtest.tmpl")

# set a value on the template instance to be displayed in the template
# -- this is how to "pass in" data to the template
t.today = datetime.now()

# Print our template instance
print t

