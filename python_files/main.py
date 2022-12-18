#from editor import add_text
from editor import del_text
#from editor import add_image
from test_editor import add_2
"""
import selenium
from selenium import webdriver
"""


'''
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.get("http://localhost:63342/pythonProject/index_page.html?_ijt=j84f308rdpajrgf7rhovuor50p")
email_form = driver.find_element_by_class_name(" box ")


#input = driver.find_element_by_name("inputbox")
#example = input.get_attribute('value')
#print(example)
'''


print("""

Список команд:
   | + добавить бумашку |
   | - удалить бумашку  |

""")

while (True):
    hello = str(input('\n' + "Команда: "))

    if hello == "add" or "+":
        user_tip = str(input("Тип файла: "))
        user_coment = str(input('Тема: '))
        user_name = str(input("Автор: "))
        add_2(user_tip, user_coment, user_name)
        print("")
        print("""Успешно добавленно)""")

    elif hello == "del" or "-":
        del_text()

    else: print("ERROR")

