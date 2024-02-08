import json


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_all(self):
        posts = self.load_data()
        return posts

    def get_by_pk(self, pk: int):
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post
        return None
