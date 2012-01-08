#!/opt/local/bin/python

from Cheetah.Template import Template

t = Template(file="commandline_example.tmpl")
t.namelist = 'Paul Yvonne Teresa Henry Ophelia Nick'.split()

print t
