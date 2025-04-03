from bs4 import BeautifulSoup
import requests

post_text = ""
url = "https://scholarslab.lib.virginia.edu/blog/"
html  = requests.get(url).text
soup = BeautifulSoup(html, features="html.parser")
old_posts_list = soup.find("section",id="previous_posts")
posts = {}
for i in old_posts_list.find_all("li"):
    # the post links are relative links, so we need to append the domain to make it an absolute link
    post_url = "https://scholarslab.lib.virginia.edu"+i.contents[0]["href"]
    print("Requesting:",post_url)
    post_html  = requests.get(post_url).text
    post_soup = BeautifulSoup(post_html, features="html.parser")
    post_title =post_soup.find("h1").get_text()
    post_text =post_soup.find("div", class_="content").get_text()
    posts[post_title] = post_text

print(posts)