import json
import requests

us_ag = {
"user-agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"platform": "Mobile", "browser": "No", "device": "Android"
}

response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
     headers={"user-agent" : us_ag["user-agent"]}
)
print(15, response.text)
json_text = json.loads(response.text)
if (json_text['platform'] == us_ag['platform']) and (json_text['browser'] == us_ag['browser']) and (json_text['device'] == us_ag['device']):
    print('Ожидаемые значения полей совпадают')
else:
    print("Параметры не совпадают \nПараметр:", "  ФР:  /", "ОР:  ")
    if json_text['platform'] != us_ag['platform']:
        print('platform', json_text['platform'], '/', us_ag['platform'])
    if json_text['browser'] != us_ag['browser']:
        print('browser', json_text['browser'], '/', us_ag['browser'])
    if json_text['device'] != us_ag['device']:
        print('device', json_text['device'], '/', us_ag['device'])

