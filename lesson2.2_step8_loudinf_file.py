from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент, кладём в переменную
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")

    # вводим в него значение
    first_name.send_keys("Иван") 

    # находим элемент, кладём в переменную
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")

    # вводим в него значение
    last_name.send_keys("Иванов")

    # находим элемент, кладём в переменную
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")

    # вводим в него значение
    email.send_keys("ivanoff@.com")

    # ищем путь к директории, в которой находится запускаемый скрипт, там же должен лежать
    # загружаемый файл, кладём в переменную
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test_file.txt')

    # находим кнопку "Выберите файл"
    choose_input = browser.find_element(By.CSS_SELECTOR, "#file")

    # отправляем файл в открытую директорию
    choose_input.send_keys(file_path)

    # нажать кнопку сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
