#!/usr/bin/python3

import cgi, cgitb 
cgitb.enable()

form = cgi.FieldStorage() 

lang = form.getvalue('lang')

print("Content-Type: plain/text")
print()

print('ahoj, testování příliš', lang)
