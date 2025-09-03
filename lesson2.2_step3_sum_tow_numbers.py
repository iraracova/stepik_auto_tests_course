from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим первое число
    number_element1 = browser.find_element(By.CSS_SELECTOR, "#num1")

    # находим текст у первого элемента
    number1 = number_element1.text 

    # находим второе число
    number_element2 = browser.find_element(By.CSS_SELECTOR, "#num2")

    # находим текст у второго элемента
    number2 = number_element2.text 

    # находим сумму двух числет, переводим их в тип числовой данных 
    sum_resalt = int(number1) + int(number2)

    # положить в переменную сумму в типе строковом типе данных
    value = str(sum_resalt)

    # находим и выбираем выпадающий список
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    
    select.select_by_visible_text(value) 
    

    # нажать кнопку сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
