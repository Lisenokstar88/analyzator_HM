#подтянули библиотеку для отправки запросов в интернет
import requests
import json
import sys
import re
from bs4 import BeautifulSoup
import urllib.request

#Константы
TITLE_NOTLINK="<div class= alert alert-info fade in role= alert >"
TITLE_RESULT="result result"
RESP=open(r"C:\Users\Мария\Desktop\python_test\resp.txt", "r+", encoding="utf-8")


#Функция определяет, есть ли результаты поиска по запросу или их нет совсем
def checkAlertInTheResponse():
    with RESP as datafile:
        for line in datafile:
            if TITLE_NOTLINK in line:
                print("Нет результатов поиска, попробуйте другой запрос")
                sys.exit
            else:
                return("true")


# функция анализирует полученные результаты поиска и собирает один файл, 
# в котором будут поля с потенциальными ссылками на ресурсы по теме запроса
def checkResponseLink():

    #преобразую список ответа на запрос в массив, в котором каждый элемент - это строка ответа
    row_list=[]
    with open(r"C:\Users\Мария\Desktop\python_test\resp.txt", "r+", encoding="utf-8") as f:
        row_list=f.readlines()

    
    
    #Объявляем пустой список(массив), в который будем добавлять, подходящие нам элементы
    #цикл проходится по файлу ответа и все строки, где есть <class "result result"> записывает в отдельный файл
    checkList=[]
    for i in row_list:
         if TITLE_RESULT in i:
             responseLink=open(r"C:\Users\Мария\Desktop\python_test\responseLink.html", "w", encoding="utf-8")
             checkList.append(i)
             responseLink.writelines(checkList)
             responseLink.close()


# #Регулярное выражение

# def regular_found_new_link():
    
#     responseLink=open(r"C:\Users\Мария\Desktop\python_test\responseLink.txt", "r+", encoding="utf-8")
#     responseLink.readline()
#     responseLink_str="".join(responseLink)
#     print(responseLink_str)
#     #Регулярное выражение, для поиска значения "href" в каждой строке из списка прошедших выборку
#     # n=re.match(r"href", responseLink_str, flags=0)
#     # if (re.findall( r'href', responseLink_str, re.M|re.I) == "true"):

    
#     for i in responseLink:
#         if (re.match("href", str) == "true"):
#             r=re.match.span("href", str)
#             print(r)

#         print(href.span())


# Инициализируем переменную со списком ссылок ресурсов по нашему запросу
def buildLinkResponseList():
    with open(r"C:\Users\Мария\Desktop\python_test\responseLink.html", "r+", encoding="utf-8")as f:

        checkList=[]
        html_page =f.read()
        soup = BeautifulSoup(html_page, "html.parser")

        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            checkList.append(link.get("href")+"\n")
            f=open(r"C:\Users\Мария\Desktop\python_test\responseLink.txt", "w", encoding="utf-8")
            f.writelines(checkList)
            f.close()