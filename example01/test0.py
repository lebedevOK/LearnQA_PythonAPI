import json
import requests
#us_ag = open("user_ag.txt", "r").readlines()
#chek1 = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}

#
# for i in us_ag:
#     response = requests.get(
#         "https://playground.learnqa.ru/ajax/api/user_agent_check",
#         headers={us_ag[User-Agent]}
#     )
#     print(response.text)
#     json_text = json.loads(response.text)
#     #json_0 = {}
    #json_0 =
    #print(json_0['browser'],json_0['browser'],json_0['device'])
    #print(json_text['browser'],json_text['browser'],json_text['device'])
    # if (json_text['platform'] == chek1['platform']) and (json_text['browser'] == chek1['browser']) and (json_text['device'] == chek1['device']):
    #     print('okOKok')
    # elif json_text['platform'] != chek1['platform']:
    #     print(json_text['platform'], '/', chek1['platform'])
    # elif json_text['browser'] != chek1['browser']:
    #     print(json_text['browser'], '/', chek1['browser'])
    # elif json_text['device'] != chek1['device']:
    #     print(json_text['device'], '/', chek1['device'])
    # else: print("stop")
########################
# us_ag = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"}
us_ag = {
"User Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"platform": "Mobile", "browser": "No", "device": "Android"
}
us_ag0 = us_ag["User Agent"]
print(us_ag0)
response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
     headers={us_ag0}
)
print(response.text)
json_text = json.loads(response.text)
if (json_text['platform'] == us_ag['platform']) and (json_text['browser'] == us_ag['browser']) and (json_text['device'] == us_ag['device']):
    print('okOKok')
elif json_text['platform'] != us_ag['platform']:
    print(json_text['platform'], '/', us_ag['platform'])
elif json_text['browser'] != us_ag['browser']:
    print(json_text['browser'], '/', us_ag['browser'])
elif json_text['device'] != us_ag['device']:
    print(json_text['device'], '/', us_ag['device'])