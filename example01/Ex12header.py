import requests

class TestHeader:

    def test_header(self):

        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        assert response.headers.get('x-secret-homework-header') == 'Some secret value', "Header invalid"