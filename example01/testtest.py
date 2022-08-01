import pytest
import json
import requests

us_ag = {"user-agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                 "platform": "Mobile", "browser": "No1", "device": "Android"
         }

class TestUserAgent:


    def test_check_useragent(self):
        us_ag0 = us_ag["user-agent"]
        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"user-agent":us_ag0}
        )
        print(response.text)
        json_text = json.loads(response.text)
        assert (json_text['platform'] == us_ag['platform']) and (json_text['browser'] == us_ag['browser']) and (json_text['device'] == us_ag['device']),\
        f"Параметры не совпадают: {json_text['platform']}/{us_ag['platform']}; {json_text['browser']}/{us_ag['browser']} ; {json_text['device']}/{us_ag['device']}"

