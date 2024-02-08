import pytest
import json


class TestApi:
    needed_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_get_all_posts(self, test_client):
        response = test_client.get("/api/posts")
        data = response.get_json()

        assert response.status_code == 200, "Стату код всех постов неверный"
        assert type(data) == list, "Тип возвращаемого значения всех постов неверный"
        assert len(data) > 0, "Возвращаемый список не пуст"
        assert set(data[0].keys()) == self.needed_keys, "Структура возвращаемых значений для всех постов неверна"

    def test_single_posts(self, test_client):
        response = test_client.get("/api/posts/1")
        data = response.get_json()
        assert response.status_code == 200, "Стату код одного поста неверный"
        assert type(data) == dict, "Тип возвращаемого значения одного поста неверный"
        assert set(data.keys()) == self.needed_keys, "Структура возвращаемого значения для одного поста неверна"
