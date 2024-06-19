# #Автотест для поиска воды


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
driver = webdriver.Chrome()
url = "https://samokat.ru/"
driver.get(url)
search_string = driver.find_element(By.CLASS_NAME,"_input_184dk_25")
search_string.send_keys("вода")
sleep(5)


