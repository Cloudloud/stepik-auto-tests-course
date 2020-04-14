from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
try: 
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    wait = WebDriverWait(browser, 12).until(
       # price = browser.find_element(By.ID, "price")
        EC.text_to_be_present_in_element((By.ID, "price"),"100")

    )
    book = browser.find_element(By.ID,"book")
    book.click()
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y= str(math.log(abs(12*math.sin(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    solve = browser.find_element_by_id("solve")
    solve.click()

  

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

