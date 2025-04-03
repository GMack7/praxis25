import requests
from bs4 import BeautifulSoup 
import csv 

base_url = "https://scholarslab.lib.virginia.edu/blog/"

# Headers to mimic a real browser request (to prevent blocking)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.get(base_url)

if response.status_code != 200:
    print(f"Failed to fetch the page: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# soup.find_all() searches the parsed HTML soup for all elements matching the given tag "a"
# "a" refers to anchor tags which create hyperlinks in HTML
# href=True ensures we only get <a> tags that have an href attribute 
posts = soup.find_all("a", href=True) 

# for each anchor tag a, we access the href attribute 
# conditional if to filter out links that include blog 
blog_links = [ a["href"] for a in soup.find_all("a", href=True) if "/blog/" in a["href"]]

# Creating Absolute URLs from Relative URLs which includes the domain for Scholars Lab 
blog_links = ["https://scholarslab.lib.virginia.edu" + link for link in blog_links]

print(blog_links)