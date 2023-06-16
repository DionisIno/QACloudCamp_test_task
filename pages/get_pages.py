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
