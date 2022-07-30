import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)

text_messages = obj['messages']
#print(text_messages) # все сообщения
key_text = text_messages[1]
# второе сообщение
print(key_text)


# Парсинг JSON пример
# string_as_json_format = '{"answer": "Hello, User"}'
# obj = json.loads(string_as_json_format)
#
# key = "answer"
# if key in obj:
#     print(obj[key])
# else:
#     print(f"Ключа {key} в JSON нет")