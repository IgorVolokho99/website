import json


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        posts = self.load_data()
        return posts

    def get_by_pk(self, pk: int):
        posts = self.get_all()
        for post in posts:
            if post["pk"] == pk:
                return post

    def get_by_word(self, word: str):
        posts = self.get_all()
        results = []
        for post in posts:
            if word.lower() in post["content"].lower():
                results.append(post)
        return results

    def get_by_username(self, username: str):
        posts = self.get_all()
        results = []
        for post in posts:
            if post["poster_name"] == username:
                results.append(post)
        return results
