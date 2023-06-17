import random


class Check:
    without_id = ["title", "userId", "body"]
    without_title = ["userId", "body"]
    id_title = ["title", "id"]
    id_title_body = ["title", "id", "body"]
    all_keys = ["title", "id", "body", "userId"]


class Data:
    only_title = {'title': 'some text'}
    title_with_body = {'title': 'some text', "body": "some text"}
    title_user_id_and_body = {f'userId': {random.randint(1, 20)}, 'title': 'some text', "body": "some text"}