from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # узнаю имя новой вкладки, кладу имя в переменную
    new_window = browser.window_handles[1]

    # переход на новую вкладку
    browser.switch_to.window(new_window)

    # нахожу текст найденного элемента с числом x, кладу в переменную
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # функция для расчета по формуле
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    # нахожу поле для ввода ответа и ввожу ответ

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)

    browser.quit()
