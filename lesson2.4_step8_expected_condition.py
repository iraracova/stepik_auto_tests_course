from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # вызываем метод, который ждет 10 секунд до появления текстового
    # значения в выбранном элементе из правила expected_condition
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # нахожу текст найденного элемента с числом x, кладу в переменную
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # функция для расчета по формуле
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    # нахожу поле для ввода ответа и ввожу ответ
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    button.submit = browser.find_element(By.CSS_SELECTOR, "#solve").click()

finally:
    time.sleep(10)

    browser.quit()
