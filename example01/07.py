import requests

### Задание 1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1. Ответ для запроса GET без параметров: ", response.text, "\n")

### Задание 2
payload2 = {"method":"HEAD"}
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload2)
print("2. Ответ для запроса HEAD: ", response2.text, "\n")

### Задание 3
payload31 = {"method":"GET"}
response31 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload31)
print("3.1. Ответ для запроса с верными параметрами для GET:", response31.text)

payload32 = {"method":"POST"}
response32 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload32)
print("3.2. Ответ для запроса с верными параметрами для POST:", response32.text)

payload33 = {"method":"PUT"}
response33 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload33)
print("3.3. Ответ для запроса с верными параметрами для PUT:", response33.text)

payload34 = {"method":"DELETE"}
response34 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload34)
print("3.4. Ответ для запроса с верными параметрами для DELETE:", response34.text, "\n")

### Задание 4
list_metods = [{"method":"GET"},{"method":"POST"},{"method":"PUT"},{"method":"DELETE"},{"method":"HEAD"},{"method":"JFDJD"}]

print("4.1. Варианты с GET запросом:")
for i in list_metods:
    response41 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(i, response41.text)

print()
print("4.2. Варианты с POST запросом:")
for i in list_metods:
    response42 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(i, response42.text)

print()
print("4.3. Варианты с PUT запросом:")
for i in list_metods:
    response43 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(i, response43.text)

print()
print("4.4. Варианты с DELETE запросом:")
for i in list_metods:
    response44 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(i, response44.text)

print()
print("4.5. Варианты с HEAD запросом:")
for i in list_metods:
    response45 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(i, response45.text)