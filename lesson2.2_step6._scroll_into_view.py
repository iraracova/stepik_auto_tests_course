from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try: 
    link = " https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент, кладём в переменную
    number_element1 = browser.find_element(By.CSS_SELECTOR, "#input_value")

    # находим текстовое значение у найденного элемента
    x = number_element1.text

    # посчитать матемалическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    # найти текстовое поле, ввести в него ответ
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # найти, проскроллить до кнопки
    button = browser.find_element(By.TAG_NAME, "button")

    browser.execute_script("return arguments[0].scrollIntoView(true, {block: 'center'});", button)

    # включить чек-бокс "I'm the robot"
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()

    # переключить радиобаттон "Robots rule"
    
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click() 

    # нажать кнопку сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
