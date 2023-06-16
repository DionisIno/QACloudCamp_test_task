import allure
from data.urls import GET_POST
from src.assertions import Assertions
from src.my_requests import MyRequests


@allure.epic("Testing GET/posts")
class TestGet:

    @allure.title("Response has status code 200")
    def test_response_has_status_code_200(self):
        """
        This test check that response has status code 200
        """
        url = f"""{GET_POST}"""
        response = MyRequests.get(url)
        Assertions.assert_code_status(response, 200)

    @allure.title("Response has status key 'id'")
    def test_response_has_key_id(self):
        """
        This test check that response has key "id"
        """
        url = f"""{GET_POST}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "id")

    @allure.title("Response has status key 'userId'")
    def test_response_has_key_user_id(self):
        """
        This test check that response has key "userId"
        """
        url = f"""{GET_POST}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "userId")

    @allure.title("Response has status key 'title'")
    def test_response_has_key_user_title(self):
        """
        This test check that response has key "userId"
        """
        url = f"""{GET_POST}"""
        response = MyRequests.get(url)
        Assertions.assert_response_has_key(response, "title")






