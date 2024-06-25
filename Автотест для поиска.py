#Автотест для поиска воды


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем сайт samokat.ru
url = "https://samokat.ru/"
driver.get(url)

# Находим поле для поиска по классам
search_string = driver.find_element(By.CLASS_NAME,"_input_184dk_25")

# Вводим  слово"вода" в строку поиска 
search_string.send_keys("вода")

# Ждем несколько секунд для закгрузки результатов поиска
sleep(5)




