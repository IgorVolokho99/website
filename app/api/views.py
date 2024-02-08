import logging
from flask import Blueprint, jsonify

from .dao.posts_dao import PostsDAO

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")

posts_dao = PostsDAO("./data/posts.json")

logger = logging.getLogger("loger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app/api/logs/api.log")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@api_blueprint.route('/api/posts')
def posts_page():
    logger.info("/api/posts")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:postid>")
def post_page(postid: int):
    logger.info(f"/api/posts/{postid}")
    post = posts_dao.get_by_pk(postid)
    if post:
        return jsonify(post)
    else:
        return "Not found"
