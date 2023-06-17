import allure
import pytest

from data.test_data import with_id
from data.urls import GET_POSTS
from src.assertions import Assertions
from src.my_requests import MyRequests


@allure.epic("Testing POST posts")
class TestPost:
    @allure.title("Creating a post without a date, checking that the answer has an id")
    def test_create_post_without_data_has_only_id(self):
        """
        This test checks that the creation of a post without a date has only id
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url)
        Assertions.assert_json_has_key(response, "id")

    @pytest.mark.parametrize("item", with_id)
    @allure.title("Creating a post without a date, checking that the answer has no keys other than id")
    def test_create_post_without_data(self, item):
        """
        This test checks that the creation of a post without a date has no keys other than id
        """
        url = f"""{GET_POSTS}"""
        response = MyRequests.post(url)
        Assertions.assert_json_has_not_key(response, item)
