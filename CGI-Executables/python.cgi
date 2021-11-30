#!/usr/bin/python

import cgi
import cgitb; cgitb.enable() # for troubleshooting

print "Content-type: text/html;charset=utf-8;"
print

print """
<html>

<head><title>Python CGI Script</title></head>

<body>

<h3> Hello, CGI form Python Script</h3>
"""

form = cgi.FieldStorage()
message = form.getvalue("message", "(no message)")

print """

<p>Previous message: %s</p>

<p>form

<form method="post" action="python.cgi">
<p>message: <input type="text" name="message"/></p>
</form>

</body>

</html>
""" % message