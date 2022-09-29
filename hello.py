#!/usr/bin/env python3

# Since this is a script to be invoked by another exec, the shebang tells the
# operating system what to interpret or run this with

import sys
import cgi
import os
import json

# Q1
# print(os.environ)

# Q2
# json_object = json.dumps(dict(os.environ))
# print(json_object)

# Create an empty dictionary
import templates

env = {}

# Iterate through environment
for env_key, env_value in os.environ.items():
    env[env_key] = env_value

# Post to itself
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")

query_string = env["QUERY_STRING"]
if query_string is not None and query_string != "":
    # show by showing any query
    print("Content-Type: text/html")
    query_string = env["QUERY_STRING"]
    body = templates.login_page()
    body += "<ul>"
    for item in query_string.split("&"):
        body += f"<li>{item}</li>"
    user_agent = env["HTTP_USER_AGENT"]
    body += f"<li>User's browser: {user_agent}</li></ul>"

    posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
    if posted_bytes:
        posted = sys.stdin.read(int(posted_bytes))
        print(f"<p> POSTED: <pre>")
        for line in posted.splitlines():
            print(line)
        print("</pre></p>")

    print(body)
else:
    print("Content-Type: application/json")
    print()

    print(json.dumps(env))