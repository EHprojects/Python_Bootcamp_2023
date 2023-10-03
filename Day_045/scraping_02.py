from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_tag = soup.find(name="a", rel="noreferrer")
# print(article_tag.getText())
# article_link = article_tag.get("href")
# print(article_link)

# get all article titles
# get all links
# get all upvote scores

titlelines = soup.findAll(name="span", class_="titleline")
score_class = soup.findAll(name="span", class_="score")

# link = titlelines[0].find(name="a").get("href")
# print(link)
# title = titlelines[0].find(name="a").getText()
# print(title)
# score_class = soup.findAll(name="span", class_="score")
# score = int(score_class[0].getText().split()[0])
# print(score)

links = []
titles = []
scores = []

for titleline in titlelines:
    link = titleline.find(name="a").get("href")
    links.append(link)
    title = titleline.find(name="a").getText()
    titles.append(title)

# for result in score_class:
#     score = int(result.getText().split()[0])
#     scores.append(score)

scores = [int(result.getText().split()[0]) for result in score_class]

# print(links)
# print(titles)
# print(scores)

high_score_idx = scores.index(max(scores))

print(titles[high_score_idx])
print(links[high_score_idx])
