import allure
from data.urls import GET_POST
from src.assertions import Assertions
from src.my_requests import MyRequests


@allure.epic("Testing GET/posts")
class TestGet:

    def test_response_has_status_code_200(self):
        url = f"""{GET_POST}"""
        response = MyRequests.get(url)
        Assertions.assert_code_status(response, 200)
