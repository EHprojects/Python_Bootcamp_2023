import requests


class Post:

    def __init__(self, post_num):
        self.post_num = post_num
        self.blog_dat = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.blog_dat)
        self.post_dat = self.response.json()

    def get_post(self):
        for post in self.post_dat:
            if post["id"] == self.post_num:
                return post
