#!/usr/bin/python
import urllib2
import requests

response = requests.get("http://www.google.ca")

print type(response)
print dir(response)
print response.status_code
