import allure
import pytest

from data.test_data import Check, Data
from data.urls import GET_POSTS
from src.assertions import Assertions
from src.my_requests import MyRequests


@allure.epic("Testing POST posts")
class TestPost:
    check = Check()
    data = Data()

    @allure.title("Creating a post without a date, checking that the answer has an id")
    def test_create_post_without_data_has_only_id(self):
        """
        This test checks that the creation of a post without a date has only id
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url)
        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 201)

    @pytest.mark.parametrize("item", check.without_id)
    @allure.title("Creating a post without a date, checking that the answer has no keys other than id")
    def test_create_post_without_data(self, item):
        """
        This test checks that the creation of a post without a date has no keys other than id
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url)
        Assertions.assert_json_has_not_key(response, item)

    @allure.title("Create a post with just a title")
    def test_create_post_with_title(self):
        """This test checks to create a post with a title only"""
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url, self.data.only_title)
        Assertions.assert_json_has_keys(response, self.check.id_title)
        Assertions.assert_code_status(response, 201)

    @pytest.mark.parametrize("item", check.without_title)
    @allure.title("Creating a post without a date, checking that the answer has no keys body and userId")
    def test_create_post_without_body_and_user_id(self, item):
        """
        This test checks that the creation of a post without a date has no keys body and userId
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url)
        Assertions.assert_json_has_not_key(response, item)

    @allure.title("Create a post with a title and body")
    def test_create_post_with_title_and_body(self):
        """This test checks to create a post with a title and body"""
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url, self.data.title_with_body)
        Assertions.assert_json_has_keys(response, self.check.id_title_body)
        Assertions.assert_code_status(response, 201)

    @pytest.mark.parametrize("elem", Check.all_keys)
    @allure.title("Create a post with a title, userId and body")
    def test_create_post_with_title_user_id_and_body(self, elem):
        """This test checks to create a post with a title, userId and body"""
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url, self.data.title_user_id_and_body)
        print(response.json())
        Assertions.assert_json_has_key(response, elem)
        Assertions.assert_code_status(response, 201)
