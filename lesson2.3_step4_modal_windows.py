from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нахожу кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # жму кнопку
    button.click()

    # переключаюсь на confirm
    confirm = browser.switch_to.alert

    # подтверждаю confirm
    confirm.accept()

    # нахожу значение x, кладу в переменную
    number = browser.find_element(By.CSS_SELECTOR, "#input_value")

    # находим текстовое значение у найденного элемента
    x = number.text

    # решаю капчу для роботов для получения числа
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x) 

    # нахожу поле для ввода ответа 
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")

    # ввожу в поле найденное значение
    input1.send_keys(y)

    # жму кнопку сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
