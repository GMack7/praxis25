import requests

url = "https://scholarslab.lib.virginia.edu/blog/"
html  = requests.get(url).text
print(html)