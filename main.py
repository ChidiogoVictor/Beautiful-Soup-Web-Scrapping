from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.prettify())
anchor_tags = soup.find_all(name="a")
# print(anchor_tags)

# for tag in anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.select(".heading")
# print(heading)

link = soup.select("p a")
print(link)

