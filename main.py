#==========================================================================================
#============================Объявляем необходимые бибилотеки==============================
#==========================================================================================

#подтянули библиотеки для отправки запросов в интернет
import requests
import json
import sys
from bs4 import BeautifulSoup
import urllib.request
import re
import pathlib
from pathlib import Path

#Получаем строку, содержащую путь к домашней директории:
dir_path = pathlib.Path.home()

#объявляем все необходимые пути к файлам
path_code_resp_txt=Path(dir_path,'code_resp.txt')
path_Helper_py=Path(dir_path,'Helper.py') #FIXME
path_max_count_txt=Path(dir_path,'max_count.txt')
path_NotResponseLin=Path(dir_path,'NotResponseLink.txt')
path_resp_html=Path(dir_path,'resp.html')
path_resp_txt=Path(dir_path,'resp.txt')
path_responseLink_html=Path(dir_path,'responseLink.html')
path_responseLink_txt=Path(dir_path,'responseLink.txt')
path_themes_txt=Path(dir_path,'themes.txt')



#==========================================================================================
#===============Отображаем графический интерфейс нашего приложения=========================
#==========================================================================================

#==========================================================================================
#====Производится сбор потенциальных источников информации, согласно введенному запросу====
#==========================================================================================

#Константы
TITLE_NOTLINK="<div class= alert alert-info fade in role= alert >"
TITLE_RESULT="result result"
RESP=open(path_resp_txt, "r+", encoding="utf-8")

class Helper():

   
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
        with open(path_resp_txt, "r+", encoding="utf-8") as f:
            row_list=f.readlines()

        
        
        #Объявляем пустой список(массив), в который будем добавлять, подходящие нам элементы
        #цикл проходится по файлу ответа и все строки, где есть <class "result result"> записывает в отдельный файл
        checkList=[]
        for i in row_list:
            if TITLE_RESULT in i:
                responseLink=open(path_responseLink_html, "w", encoding="utf-8")
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
        with open(path_responseLink_html, "r+", encoding="utf-8")as f:

            checkList=[]
            html_page =f.read()
            soup = BeautifulSoup(html_page, "html.parser")

            for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
                checkList.append(link.get("href")+"\n")
                f=open(path_responseLink_txt, "w", encoding="utf-8")
                f.writelines(checkList)
                f.close()





#==========================================================================================
#====Производится сбор потенциальных источников информации, согласно введенному запросу====
#==========================================================================================

print("1")
#считываем возможные тематики
themes=open(path_themes_txt, "r+", encoding="utf-8")

print("2")
#просим ввести запрос для определения тематики
print("Введите запрос для определения тематики")

# #считываем введенный запрос в переменную и преобразовываем её в текст
message=input()


#Проверяем, что в сообщение переданы буквы или цфиры, иначе выключаем программу
if not isinstance(message, str) and not isinstance(message, int):
    print("Ошибка: Сообщение не содержит букв или цифр")
    sys.exit()

#задали переменной параметров библиотеку готовых параметров
params = dict(q=message)

#производим запрос в поисковую систему SEARX по нашему ключевому сообщению
url= "https://searx.roughs.ru/search"

#результаты полученные от сервиса поиска SEARX кладу в переменную "res"
res = (requests.get(url, params=params))

#открываю файл для хранения статуса ответа и записываю в него статус ответа, 
#после чего обязательно закрываю его, чтобы изменения сохранились
code_resp=open(path_code_resp_txt, "r+", encoding="utf-8")
code_resp.write(str(res.status_code))
code_resp.close()

#вновь открываю файл со статусом ответа, чтобы увидеть появившийся код и считываю его в переменную code_resp_str
code_resp=open(path_code_resp_txt, "r+", encoding="utf-8")
code_resp_str=code_resp.read()

#функция проверяет код ответа на успешность или ошибку
if (code_resp_str[0]=="2"):
    print("тут реакция на 200-ую")
elif (code_resp_str[0]=="5"):
    print("тут реакция на 500-ую")
else:
    print("тут реакция на 400-ую")


    #в переменную положил конкретное поле ответа "text", в котором лежит весь контент ответа
res_text=res.text

    #открываю файл для записи ответа по запросу, записываю туда ответ и закрываю файл 
resp=open(path_resp_txt, "r+", encoding="utf-8")
resp.write(res_text)
resp.close()



#==========================================================================================
#================================Подготовка к сбору информации=============================
#==========================================================================================

    #Проверяем, есть ли результаты поиска по запросу или их нет совсем.
    #Если есть - вызываем функцию для анализа полученных результатов поиска
if (Helper.checkAlertInTheResponse() =="true"):
    print("true")

    # функция анализирует полученные результаты поиска и собирает один файл, 
    # в котором будут поля с потенциальными ссылками на ресурсы по теме запроса
Helper.checkResponseLink()

    # Инициализируем переменную со списком ссылок ресурсов по нашему запросу
Helper.buildLinkResponseList()

    # resp=open(r"C:\Users\Мария\Desktop\python_test\responseLink.txt", "r+", encoding="utf-8")
    # lb2=tk.Label(window, text=res)
    # lb1.grid(column=0, row=2)

    #==========================================================================================
    #================================Сбор информации для анализа===============================
    #==========================================================================================

    # from urllib 
