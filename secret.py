#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
import os
import sys
cgitb.enable()

class FollowingTheTAsInstructionsError(Exception):
    def __init__(self):
        Exception.__init__(self, (
            "You must edit secret.py to change the username, password, "
            "and to delete this error!"
        ))

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")

# Edit the following two lines:
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")