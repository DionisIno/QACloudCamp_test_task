import allure
from requests import Response


class GetPages:
    @allure.step("Checking the number of posts per user id")
    def check_user_id_has_10_posts(self, response: Response, elem):
        """This method checks the number of posts per user id"""
        response_json = response.json()
        count = 0
        for item in response_json:
            if item["userId"] == elem:
                count += 1
        assert count == 10, f"The number of posts of one user ID is not equal to 10, it is equal to {count}"

    @allure.step("Checks that each title and body is not empty")
    def check_each_title_and_body_in_the_response_is_not_empty(self, response: Response, elem):
        """This method checks that each title and body is not empty"""
        response_json = response.json()
        for item in response_json:
            assert len(item[elem]) > 0, f"{item[elem]} in {item} is empty"
