from flask import Blueprint, render_template, request

from .dao.posts_dao import PostsDAO
from .dao.comments_dao import CommentsDAO

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

posts_dao = PostsDAO("./data/posts.json")
comments_dao = CommentsDAO("./data/comments.json")


@main_blueprint.route('/')
def main_page():
    posts = posts_dao.get_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid: int):
    post = posts_dao.get_by_pk(postid)
    comments = comments_dao.get_by_post_pk(postid)
    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route('/search')
def search_page():
    s = request.values.get('s', "None")
    posts = posts_dao.get_by_word(s)
    return render_template("search.html", posts=posts)


@main_blueprint.route("/users/<string:username>")
def user_page(username: str):
    posts = posts_dao.get_by_username(username)
    return render_template("user-feed.html", posts=posts)


