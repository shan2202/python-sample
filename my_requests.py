
import requests
import os
import sys

res = requests.get("http://www.google.com")
with open("google.html",mode='w') as f:
    f.write(res.text)
