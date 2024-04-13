import requests
from flask import Flask, render_template
from Day_057.post import Post

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def get_post(num):
    post_dat = Post(num).get_post()
    # print(post_dat)
    return render_template("post.html", post_dat=post_dat)


if __name__ == "__main__":
    app.run(debug=True)
