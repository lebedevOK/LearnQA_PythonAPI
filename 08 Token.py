import requests
import json
import time
import sys

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print("Задача создана")
#print(response.text)
print()
#time.sleep(10) # активировать для проверки альтернативного сценария
json_text = response.text
obj = json.loads(json_text)
payload = {"token":obj['token']}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)

status_text = response2.text
status1 = json.loads(status_text)
if status1['status'] == "Job is NOT ready":
    print("Мы про вас помним, задача в работе, ожидайте")
elif status1['status'] == "Job is ready" and status1['result']:
    payload = {"token": obj['token']}
    response4 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    print("Задача готова, результат:", status1['result'])
    sys.exit()
else:
    print('Что-то пошло не по плану, неизвестный статус.')
    sys.exit()

print('Время ожидания:',obj['seconds'], "сек.", "\n")
time.sleep(obj['seconds'])

payload = {"token":obj['token']}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)

status_text = response3.text
status2 = json.loads(status_text)
if status2['status'] == "Job is ready" and status2['result']:
    print("Задача готова, результат:", status2['result'])



