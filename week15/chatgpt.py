import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict
from datetime import datetime

# Base URL for the Scholars' Lab blog
base_url = "https://scholarslab.lib.virginia.edu/blog/"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Request the main page
response = requests.get(base_url, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch the page: {response.status_code}")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all links containing "/blog/" (blog links)
blog_links = [
    "https://scholarslab.lib.virginia.edu" + a["href"]
    for a in soup.find_all("a", href=True)
    if "/blog/" in a["href"]
]

# Remove duplicates
blog_links = list(set(blog_links))

# List to store blog data and month-wise word counts
blog_data = []
monthly_word_count = defaultdict(int)

# Scrape each blog post
for blog_url in blog_links:
    print(f"Fetching: {blog_url}")
    
    try:
        blog_response = requests.get(blog_url, headers=headers)
        
        if blog_response.status_code != 200:
            print(f"Failed to fetch {blog_url} (Status: {blog_response.status_code})")
            continue

        blog_soup = BeautifulSoup(blog_response.text, "html.parser")
        
        # Extract blog title
        title_tag = blog_soup.find("h1")
        blog_title = title_tag.get_text(strip=True) if title_tag else "Untitled"

        # Extract author from a known class (Update this based on actual HTML structure)
        author_tag = blog_soup.find(class_="author")  # Change class_ to the actual author class
        blog_author = author_tag.get_text(strip=True) if author_tag else "Unknown"

        # Debugging: Print found authors
        print(f"Author found: {blog_author}")

        # Only process blogs written by Brandon Walsh
        if "Brandon Walsh" not in blog_author:
            print(f"Skipping {blog_url} (Author: {blog_author})")
            continue

        # Extract blog content
        content_tag = blog_soup.find("div", class_="content")
        blog_text = content_tag.get_text(strip=True) if content_tag else "No content found"

        # Extract date of publication
        date_tag = blog_soup.find("time")
        blog_date = date_tag["datetime"] if date_tag else "Unknown"
        
        # Convert date to Month-Year format (e.g., "2025-04")
        try:
            post_date = datetime.fromisoformat(blog_date)
            month_year = post_date.strftime("%Y-%m")  # e.g., '2025-04'
        except ValueError:
            month_year = "Unknown"
        
        # Count words in the blog post
        word_count = len(blog_text.split())

        # Update monthly word count
        monthly_word_count[month_year] += word_count

        # Limit the blog content length
        blog_text = blog_text[:1000] + "..." if len(blog_text) > 1000 else blog_text

        # Append data to list
        blog_data.append([blog_title, blog_url, blog_text, blog_date, word_count])

    except Exception as e:
        print(f"Error processing {blog_url}: {e}")

# Save blog data to CSV
csv_filename = "brandon_walsh_blogs.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL", "Content", "Date", "Word Count"])
    writer.writerows(blog_data)

# Save monthly word count to a separate CSV
monthly_csv_filename = "monthly_word_count.csv"
with open(monthly_csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Total Word Count"])
    for month, count in sorted(monthly_word_count.items()):
        writer.writerow([month, count])

print(f"Scraped {len(blog_data)} blog posts by Brandon Walsh and saved to {csv_filename}")
print(f"Monthly word count saved to {monthly_csv_filename}")