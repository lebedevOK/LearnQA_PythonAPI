import requests

class TestCookie:

    def test_cookie(self):

        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert response.cookies.get('HomeWork') == 'hw_value', "Cookie invalid"