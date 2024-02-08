import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        comments = self.load_data()
        return comments

    def get_by_pk(self, pk: int):
        comments = self.load_data()
        for comment in comments:
            if comment["pk"] == pk:
                return comment

    def get_by_post_pk(self, post_pk: int):
        comments = self.load_data()
        results = []
        for comment in comments:
            if comment["post_id"] == post_pk:
                results.append(comment)
        return results
