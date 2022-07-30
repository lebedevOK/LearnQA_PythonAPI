import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect") #, allow_redirects=True
response1 = response.history[0]
response2 = response.history[1]
all_responses = response.history
count = len(all_responses)

print("Переходы: ")
#print(all_responses)
print(response1.url, all_responses[0])
print(response2.url, all_responses[1])
print("Всего переходов: ", count)

print("Конечный url: ", response.url)

