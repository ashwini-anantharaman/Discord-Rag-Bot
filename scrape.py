import requests
from bs4 import BeautifulSoup
import os

os.makedirs("docs", exist_ok=True)

index = requests.get("http://paulgraham.com/articles.html")
soup = BeautifulSoup(index.text, "html.parser")
links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].endswith(".html")]

for link in links:
    url = f"http://paulgraham.com/{link}"
    try:
        page = requests.get(url)
        text = BeautifulSoup(page.text, "html.parser").get_text()
        filename = link.replace(".html", ".txt")
        with open(f"docs/{filename}", "w") as f:
            f.write(text)
        print(f"Saved {filename}")
    except:
        print(f"Skipped {link}")
