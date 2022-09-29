#!/usr/bin/env python3

# Since this is a script to be invoked by another exec, the shebang tells the
# operating system what to interpret or run this with

import sys
import os
import json

# Q1
# print(os.environ)

# Q2
# json_object = json.dumps(dict(os.environ))
# print(json_object)

# Create an empty dictionary
env = {}

# Iterate through environment
for env_key, env_value in os.environ.items():
    env[env_key] = env_value

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")

print("Content-Type: application/json")
print()

print(json.dumps(env))