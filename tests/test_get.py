import allure
import pytest

from data.urls import GET_POSTS
from pages.get_pages import GetPages
from src.assertions import Assertions
from src.my_requests import MyRequests


@allure.epic("Testing GET/posts")
class TestGet:
    page = GetPages()

    @allure.title("Response has status code 200")
    def test_response_has_status_code_200(self):
        """
        This test check that response has status code 200
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        Assertions.assert_code_status(response, 200)

    @allure.title("Response has status key 'id'")
    def test_response_has_key_id(self):
        """
        This test check that response has key "id"
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "id")

    @allure.title("Response has status key 'userId'")
    def test_response_has_key_user_id(self):
        """
        This test check that response has key "userId"
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "userId")

    @allure.title("Response has status key 'title'")
    def test_response_has_key_title(self):
        """
        This test check that response has key "title"
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "title")

    @allure.title("Response has status key 'body'")
    def test_response_has_key_body(self):
        """
        This test check that response has key "body"
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "body")

    @allure.title("Response has be json format")
    def test_response_is_json(self):
        """
        This test checks that the response is json"
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_be_json(response)

    @pytest.mark.parametrize("elem", range(1, 11))
    @allure.title("Each user id has 10 posts")
    def test_heck_every_user_id_has_10_posts(self, elem):
        """
        This test checks that each user id has 10 posts
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.get(url)
        self.page.check_user_id_has_10_posts(response, elem)
