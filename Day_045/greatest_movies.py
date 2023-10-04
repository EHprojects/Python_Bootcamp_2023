import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
best_movies = response.text
soup = BeautifulSoup(best_movies, "html.parser")

movie_list = soup.find(name="div", class_="entity-info-items__list")
# print(movie_list)
movies = []

movie_links = movie_list.find_all(name="a")
for movie in movie_links:
    movie_name = movie.getText()
    movies.append(movie_name)

# print(movies)

with open("movies.txt", "w") as file:
    rank = 1
    for movie in movies[::-1]:
        file.write(f"{rank}) {movie}\n")
        rank += 1
