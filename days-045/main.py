from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

#                   section 2 begin
#
# response = requests.get("https://news.ycombinator.com/show")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a", class_="titlelink")
# article_text = []
# article_link = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_text.append(text)
#     link = article_tag.get("href")
#     article_link.append(link)
#
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
# # print(largest_index)
#
#
# print(article_text[largest_index])
# print(article_link[largest_index])
# print(article_upvotes[largest_index])
#
# # print(int(article_upvotes[0]))
#
#           section 2 end




#           section 1 begin
#
# import lxml
#
# # with open("website.html") as file:
# #     contents = file.read()
#
# file = codecs.open("website.html", "r", "utf-8")
# contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# heading = soup.select(".heading")
# print(heading)
#
#
