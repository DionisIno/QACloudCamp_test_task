import allure

from data.test_data import Data
from data.urls import GET_ID
from src.assertions import Assertions
from src.my_requests import MyRequests


@allure.epic("Testing delete")
class TestDelete:
    data = Data()

    @allure.title("Response has status code 200 after delete")
    def test_delete_post_status_code_200(self):
        """
        This test checks the status of the code after deleting a post
        """
        url = f"""{GET_ID}"""
        response = MyRequests.delete(url)
        Assertions.assert_code_status(response, 200)

    @allure.title("Response has empty json after delete")
    def test_delete_post_has_empty_json(self):
        """
        This test checks that come empty json after deleting a post
        """
        url = f"""{GET_ID}"""
        response = MyRequests.delete(url)
        Assertions.assert_empty_json(response)
